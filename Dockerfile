FROM python:3.9

WORKDIR /app
COPY . .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

RUN pip install --upgrade pip && \
    pip cache purge && \
    pip install -r requirements.txt

CMD ["python", "app/main.py"]
