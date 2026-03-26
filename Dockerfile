FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]

RUN apt-get update && apt-get install -y curl

HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1
