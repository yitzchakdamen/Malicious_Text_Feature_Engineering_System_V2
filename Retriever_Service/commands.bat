docker network create KafkaNewsStream20

docker stop kafka-broker
docker rm kafka-broker


python -m Retriever_Service.app.main