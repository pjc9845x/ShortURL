# ShortenURL (Client Program)

# To export to executable, run this command: python -O -m PyInstaller --onefile shorturl_client.py

import requests

def shortenURL():
    url=input("Enter the name of the address: ")
    print("\n")
    try:
        response = requests.post("http://localhost:8000/shorten", json={"url": url}, timeout=5)
        response.raise_for_status()
        data=response.json()
        shortURL=data["url"]
        return data['url'].split('/')[-1]  # Extract short code
    except requests.exceptions.RequestException as e:
        print("Error connecting to server! Is Docker on?")
        print({e})
        return None

def getOriginalURL(shortCode):
    try:
        response = requests.get(f"http://localhost:8000/{shortCode}", timeout=5)
        response.raise_for_status()
        print(f"Redirecting to: {response.url}")
    except requests.exceptions.RequestException as e:
        print("Error: Unable to retrieve the original URL. Make sure Docker is running.")
        print(f"Details: {e}")

def getURLStats(shortCode):
    try:
        response = requests.get(f"http://localhost:8000/status/{shortCode}", timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"Short Code: {data['Short code']}")
        print(f"Visits: {data['Visits']}")
    except requests.exceptions.RequestException as e:
        print("Error connecting to server! Is Docker on?")
        print({e})




print("ShortURL - Client Program")

print("Note: Make sure the ShortURL server program is up and running. Just go to command, and enter 'docker-compose up --build -d' in terminal to start it. Docker must be installed.")

while True:
    print("1: Shorten URL")
    print("2: Get Original URL")
    print("3: URL Stats")
    print("4: Exit\n")

    choice=input("Enter Choice: ")
    print("\n")
    if choice=='1':
        shortenedURL=shortenURL()
        print(f"New shortened URL: {shortenedURL}\n")
    elif choice=='2':
        if 'shortenedURL' in locals() and shortenedURL:
            getOriginalURL(shortenedURL)
        else:
            print("No shortened URL found!")
    elif choice=='3':
        if 'shortenedURL' in locals() and shortenedURL:
            getURLStats(shortenedURL)
        else:
            print("No shortened URL found!")
    elif choice=='4':
        print("Goodbye!")
        break
    else:
        print("Sorry, invalid choice. Try again.")
    print("-------------------------------")