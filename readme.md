# Short URL - A Simple URL Shortener

Short URL is a simple URL shortening service built using Flask and Redis. It allows users to shorten long URLs and track the number of times a short URL has been accessed.

## 🚀 Features
- Shorten any URL
- Redirect from short URL to the original URL
- Track the number of visits for each shortened URL
- Built using Flask and Redis
- Fully containerized with Docker and Docker Compose
- Can be converted into an executable using PyInstaller

## 🛠 Installation
### **1. Pull the Repository**
```sh
git clone https://github.com/pjc9845x/ShortURL
cd shorturl
```

## **2. Installing Dependencies**

### **For Those Who Have Python Installed**
Ensure you have Python 3.9+ installed, then install dependencies:
```sh
pip install -r requirements.txt
```

### **For Those Who Do Not Have Python Installed (Run the Executable)**
If you don’t have Python, you can run the pre-built executable:
1. Download the latest `shorturl_app.exe` (Windows) or `shorturl_app` (Linux/macOS) from the **Releases** section in the repository.
2. Move the file to your preferred directory.
3. Run the executable:
   ```sh
   ./shorturl_app  # On macOS/Linux
   shorturl_app.exe  # On Windows
   ```

## 🐳 Running the Application with Docker

### **1. Build and Run the Container**
If you don’t have Redis installed, you can run everything with Docker:
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

## 🎯 Running the Program
### **For Python Users**
```sh
python shorturl.py
```
The app will be running at **http://localhost:8000**.

### **For Non-Python Users (Run the Executable)**
1. Navigate to the directory containing `shorturl_app`.
2. Run:
   ```sh
   ./shorturl_app  # On macOS/Linux
   shorturl_app.exe  # On Windows
   ```

## 🖥️ How to Operate the Program
After launching the program, you will be prompted with options:

1️⃣ **Shorten a URL**
   - Enter the URL to shorten, and receive a short URL.

2️⃣ **Retrieve the Original URL**
   - Use the short code to retrieve the original URL.

3️⃣ **Check URL Statistics**
   - View the visit count for a given short URL.

4️⃣ **Exit the Program**
   - Exit the interactive client.

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

## 🛑 Stopping and Removing Containers
To stop all containers:
```sh
docker-compose down
```
To remove all Redis data:
```sh
docker volume rm redis_data
```


---
