FROM python:3.11-slim

WORKDIR /app


COPY Preprocessor_Service/requirements.txt .
RUN pip install -r requirements.txt

COPY Kafka_Tools /app/Kafka_Tools
COPY Text_cleaned_and_processed /app/Text_cleaned_and_processed

COPY Preprocessor_Service /app/Preprocessor_Service

CMD ["python", "-m", "Preprocessor_Service.app.main"]
