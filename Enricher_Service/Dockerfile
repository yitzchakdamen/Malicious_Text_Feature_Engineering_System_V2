FROM python:3.11-slim

WORKDIR /app


COPY Enricher_Service/requirements.txt .
RUN pip install -r requirements.txt

ENV NLTK_DATA=/usr/local/share/nltk_data
RUN python -m nltk.downloader -d /usr/local/share/nltk_data vader_lexicon

COPY Kafka_Tools /app/Kafka_Tools
COPY Text_cleaned_and_processed /app/Text_cleaned_and_processed

COPY Enricher_Service /app/Enricher_Service

CMD ["python", "-m", "Enricher_Service.app.main"]
