# Short URL - A Simple URL Shortener

Short URL is a simple URL shortening service built using Flask and Redis. It allows users to shorten long URLs and track the number of times a short URL has been accessed.

## 🚀 Features
- Shorten any URL
- Redirect from short URL to the original URL
- Track the number of visits for each shortened URL
- Built using Flask and Redis
- Fully containerized with Docker and Docker Compose
- Can be converted into an executable using PyInstaller

## 🛠 Pulling and Installing
### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/shorturl.git
cd shorturl
```

### **2. Install Dependencies (Without Docker)**
Ensure you have Python 3.9+ installed, then install dependencies:
```sh
pip install -r requirements.txt
```

### **3. Run Redis (via Docker)**
If you don’t have Redis installed, you can run it using Docker:
```sh
docker run -d --name myredis -p 6379:6379 redis
```
If you're using **Windows**, update `shorturl.py` to use:
```python
redisClient = rd.StrictRedis(host='host.docker.internal', port=6379, db=0, decode_responses=True)
```

### **4. Running the Flask App (Without Docker)**
```sh
python shorturl.py
```
The app will be running at **http://localhost:8000**.

## 🐳 Running the Container
### **1. Build and Run Using Docker Compose**
```sh
docker-compose up --build -d
```
Now both Flask and Redis are running inside Docker.

### **2. Verify Everything is Working**
Check running containers:
```sh
docker ps
```
Test Redis inside the container:
```sh
docker exec -it redis_server redis-cli
PING
```
It should return:
```
PONG
```

### **3. Stopping and Removing Containers**
To stop all containers:
```sh
docker-compose down
```
To remove all Redis data:
```sh
docker volume rm redis_data
```

## 🐍 Running as an Executable with PyInstaller
If you want to create a standalone executable of the application using **PyInstaller**, follow these steps:

### **1. Install PyInstaller**
```sh
pip install pyinstaller
```

### **2. Build the Executable**
Run the following command to create a standalone executable:
```sh
pyinstaller --onefile --name shorturl_app shorturl.py
```

### **3. Run the Executable**
After the build is complete, navigate to the `dist` folder and run the executable:
```sh
cd dist
./shorturl_app  # On macOS/Linux
shorturl_app.exe  # On Windows
```
The app should now run without needing Python.

## 🧪 Testing with Postman or Curl
### **Shorten a URL**
```sh
curl -X POST http://localhost:8000/shorten -H "Content-Type: application/json" -d '{"url": "https://example.com"}'
```
Response:
```json
{
    "url": "http://localhost:8000/abc123"
}
```

### **Access a Shortened URL**
```sh
curl -L http://localhost:8000/abc123
```

### **Check Visit Count**
```sh
curl http://localhost:8000/status/abc123
```
Response:
```json
{
    "Short code": "abc123",
    "Visits": 1
}
```

## 🤝 Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a Pull Request

## 📜 License
This project is licensed under the MIT License.

---

Happy coding! 🚀
