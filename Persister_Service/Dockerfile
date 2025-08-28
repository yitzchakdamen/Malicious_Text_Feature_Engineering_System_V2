FROM python:3.11-slim

WORKDIR /app


COPY Persister_Service/requirements.txt .
RUN pip install -r requirements.txt

COPY Kafka_Tools /app/Kafka_Tools
COPY Text_cleaned_and_processed /app/Text_cleaned_and_processed

COPY Persister_Service /app/Persister_Service

CMD ["python", "-m", "Persister_Service.app.main"]
