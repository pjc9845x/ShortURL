# Short URL
import fastapi as ap
import flask as fs
import pydantic as pd
import redis as rd
import random
import string
import requests as rq

app=fs.Flask(__name__)

redisClient=rd.StrictRedis(host='redis', port=6379, db=0,decode_responses=True) # Connect to Redis


class URLRequest (pd.BaseModel):
    url:pd.HttpUrl

def genShortCode(length=6):
    characters=string.ascii_letters+string.digits
    return ''.join(random.choices(characters,k=length))


@app.route('/shorten', methods=['POST'])
def shortenURL():
    data=fs.request.get_json()
    longURL=data.get('url')

    if not longURL:
        return fs.jsonify({'ERROR': 'MISSING URL'}), 400
    
    shortCode=genShortCode()
    while redisClient.exists(shortCode):
        shortCode=genShortCode()

    redisClient.set(shortCode, longURL)

    # Map in Redis
    redisClient.set(shortCode, longURL)
    redisClient.set(f"count: {shortCode}", 0)

    shortenURL=f"http://localhost:8000/{shortCode}"
    return fs.jsonify({"url": shortenURL})

@app.route('/<shortCode>', methods=['GET'])
def redirectToLongURL(shortCode):
    longURL=redisClient.get(shortCode)

    if not longURL:
        return fs.jsonify({"ERROR": "Shortened URL NOT FOUND :("})
    
    redisClient.incr(f"count:{shortCode}")

    return fs.redirect(longURL)

# Get Statistics
@app.route('/status/<shortCode>', methods=['GET'])
def getStats(shortCode):
    if not shortCode:
        return fs.jsonify({"ERROR": "Shortened URL NOT FOUND :("})

    fs.redirect({"Short URL": shortCode})

    
    count=redisClient.get(f"count:{shortCode}")
    return fs.jsonify({"Short code": shortCode, "Visits": int(count)})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)