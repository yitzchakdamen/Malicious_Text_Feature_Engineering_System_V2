FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --upgrade kafka-python

COPY . app/Retriever_Service
COPY C:\Users\isaac\source\repos\Malicious_Text_Feature_Engineering_System_V2\Kafka_Tools /app/Kafka_Tools

CMD ["python", "-m", "app.Retriever_Service.app.main"]