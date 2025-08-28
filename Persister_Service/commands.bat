docker network create KafkaNewsStream20

docker stop kafka-broker
docker rm kafka-broker

cd C:\Users\isaac\source\repos\Malicious_Text_Feature_Engineering_System_V2
python -m Persister_Service.app.main

docker build -t app-subscribers .

docker run -d --name app-subscribers-1 ^
    -e APP_SUB_HOST=0.0.0.0 ^
    -e APP_SUB_PORT=8001 ^
    -e KAFKA_BOOTSTRAP_SERVERS=kafka-broker:9092 ^
    -e KAFKA_TOPIC=interesting_news ^
    -e MONGO_HOST=mongodb-NewsStream20 ^
    -e MONGO_PORT=27017 ^
    -e MONGO_DATABASE=NewsStream20Public ^
    -e GROUP=group_interesting_news_1 ^
    --network KafkaNewsStream20 ^
    -p 8001:8001 app-subscribers