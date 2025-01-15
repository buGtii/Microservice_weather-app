# Microservice_weather-app
 here I have used my docker username in the place of username which is "faisal991".
This repository contains a microservice which is weather app.
Here is a step-by-step guide to build, run, push, and pull a weather app using your Docker
Hub :

```markdown
# Weather App

The Weather App is a Flask-based application that retrieves current weather data for a given city using the OpenWeatherMap API. This guide walks you through building, running, and deploying the app using Docker.

---

## Prerequisites
1. Docker installed on your system.
2. OpenWeatherMap API key (replace `your_openweathermap_api_key` in `app.py`).

---

## Installation and Setup

### 1. Create the Python Application
1. Create a file named `app.py`:
```bash
nano app.py
```

2. Add the following code:
```python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    data = response.json()
    return jsonify({
        "city": city,
        "temperature": data['main']['temp'],
        "description": data['weather'][0]['description']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

## Docker Setup

### 2. Create a Dockerfile
1. Create a file named `Dockerfile`:
```bash
nano Dockerfile
```

2. Add the following content:
```dockerfile
# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app.py /app

# Install required Python packages
RUN pip install flask requests

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
```

---

### 3. Build and Run the Docker Image

#### Build the Docker Image:
```bash
docker build -t faisal991/weather-app .
```

#### Run the Docker Container:
```bash
docker run -d -p 5000:5000 faisal991/weather-app
```

#### Test the Application:
```bash
curl "http://localhost:5000/weather?city=London"
```

Expected response:
```json
{
    "city": "London",
    "temperature": 8.5,
    "description": "clear sky"
}
```

---

## Deploying to Docker Hub

### 4. Push the Image to Docker Hub
1. Tag the image:
```bash
docker tag faisal991/weather-app faisal991/weather-app:latest
```

2. Push the image:
```bash
docker push faisal991/weather-app:latest
```

---

## Pulling and Running the App on Another System

### 5. Pull and Run the Image
1. Pull the image:
```bash
docker pull faisal991/weather-app:latest
```

2. Run the container:
```bash
docker run -d -p 5000:5000 faisal991/weather-app:latest
```

3. Test the app:
```bash
curl "http://localhost:5000/weather?city=London"
```

---

## Optional: Using Docker Compose

### 6. Create a Docker Compose File
1. Create a file named `docker-compose.yml`:
```bash
nano docker-compose.yml
```

2. Add the following content:
```yaml
version: '3.8'

services:
  weather-app:
    image: faisal991/weather-app:latest
    ports:
      - "5000:5000"
```

3. Start the service:
```bash
docker-compose up -d
```

---

## Stopping and Cleaning Up

### Stop and Remove Containers:
```bash
docker ps
docker stop <container_id>
docker rm <container_id>
```

### Remove the Image:
```bash
docker rmi faisal991/weather-app:latest
```


