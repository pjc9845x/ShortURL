# Use official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy application files to container
COPY shorturl.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8000 for Flask
EXPOSE 8000

# Run the application
CMD ["python", "shorturl.py"]