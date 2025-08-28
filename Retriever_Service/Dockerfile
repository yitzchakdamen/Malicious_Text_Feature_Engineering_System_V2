FROM python:3.11-slim

WORKDIR /app


COPY Retriever_Service/requirements.txt .
RUN pip install -r requirements.txt

COPY Kafka_Tools /app/Kafka_Tools

COPY Retriever_Service /app/Retriever_Service

CMD ["python", "-m", "Retriever_Service.app.main"]
