@REM ---- Enricher_Service ----

cd C:\Users\isaac\source\repos\Malicious_Text_Feature_Engineering_System_V2
docker build -t enricher-service -f Enricher_Service/Dockerfile .

docker network create Week_11_Kafka_Malicious_Text

docker stop enricher-service
docker rm enricher-service

docker run -d --name enricher-service ^
    -e KAFKA_BOOTSTRAP_SERVERS=kafka-broker:9092 ^
    -e COL_NAME_TO_PROCESS=clean_text ^
    -e TOPIC_A=preprocessed_tweets_antisemitic ^
    -e TOPIC_B=preprocessed_tweets_not_antisemitic ^
    -e KAFKA_GROUP_ID=group_Enricher ^
    --network Week_11_Kafka_Malicious_Text ^
    enricher-service:latest

docker login
docker tag enricher-service:latest yitzchakdamen/enricher-service:latest
docker push yitzchakdamen/enricher-service:latest

docker 