
@REM ---- retriever-service ----

docker network create Week_11_Kafka_Malicious_Text

docker stop retriever-service
docker rm retriever-service

cd C:\Users\isaac\source\repos\Malicious_Text_Feature_Engineering_System_V2
docker build -t retriever-service -f Retriever_Service/Dockerfile .

docker run -d --name retriever-service ^
    -e APP_SUB_HOST=0.0.0.0 ^
    -e APP_SUB_PORT=8001 ^
    -e KAFKA_BOOTSTRAP_SERVERS=kafka-broker:9092 ^
    -e KAFKA_TOPIC=interesting_news ^
    -e MONGO_HOST=mongodb-NewsStream20 ^
    -e MONGO_PORT=27017 ^
    -e MONGO_DATABASE=NewsStream20Public ^
    -e GROUP=group_interesting_news_1 ^
    --network Week_11_Kafka_Malicious_Text ^
    retriever-service:latest
