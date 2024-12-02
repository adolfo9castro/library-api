FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=run.py

ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python", "run.py"]

