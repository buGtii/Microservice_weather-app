This file contains the code for Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY app.py /app
RUN pip install flask requests
EXPOSE 5000
CMD ["python", "app.py"]
