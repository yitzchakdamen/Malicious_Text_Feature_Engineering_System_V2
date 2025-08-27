FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --upgrade kafka-python

COPY . .
COPY "../Kafka_Tools" .

CMD ["python", "-m", "app.Retriever_Service.app.main"]