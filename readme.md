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
### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/shorturl.git
cd shorturl
```

### **2. Pull and Install Dependencies**
If using Docker, ensure you have Docker installed and pull the latest Redis image:
```sh
docker pull redis:latest
```
If running locally, install dependencies:
```sh
pip install -r requirements.txt
```

### **3. Run Redis (via Docker)**
```sh
docker run -d --name myredis -p 6379:6379 redis
```
If you're using **Windows**, update `shorturl.py` to use:
```python
redisClient = rd.StrictRedis(host='host.docker.internal', port=6379, db=0, decode_responses=True)
```

### **4. Running the Application**
#### **Run the Flask App (Without Docker)**
```sh
python shorturl.py
```
The app will be running at **http://localhost:8000**.

## 🐳 Running Everything with Docker
### **1. Create a `Dockerfile`**
```dockerfile
# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask redis requests pydantic

# Expose the application port
EXPOSE 8000

# Run the Flask application
CMD ["python", "shorturl.py"]
```

### **2. Create a `docker-compose.yml` File**
```yaml
version: '3.8'

services:
  web:
    build: .
    container_name: shorturl_app
    ports:
      - "8000:8000"
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis
      - FLASK_ENV=production

  redis:
    image: redis:latest
    container_name: redis_server
    restart: always
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: ["redis-server", "--appendonly", "yes"]

volumes:
  redis_data:
    driver: local
```

### **3. Build and Run the Container**
```sh
docker-compose up --build -d
```
Now both Flask and Redis are running inside Docker.

### **4. Verify Everything is Working**
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

## 🛑 Stopping and Removing Containers
To stop all containers:
```sh
docker-compose down
```
To remove all Redis data:
```sh
docker volume rm redis_data
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
