FROM python:3.13.14-slim

WORKDIR /app

RUN apt-get update && apt-get install chromium -y \
chromium-driver && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
