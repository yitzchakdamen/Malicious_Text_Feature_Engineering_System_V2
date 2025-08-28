FROM python:3.11-slim

WORKDIR /app


COPY DataRetrieval_Service/requirements.txt .
RUN pip install -r requirements.txt

COPY Kafka_Tools /app/Kafka_Tools
COPY Text_cleaned_and_processed /app/Text_cleaned_and_processed

EXPOSE 8000

COPY DataRetrieval_Service /app/DataRetrieval_Service

CMD ["python", "-m", "DataRetrieval_Service.app.main"]
