@REM ---- Persister_Service ----

cd C:\Users\isaac\source\repos\Malicious_Text_Feature_Engineering_System_V2
docker build -t persister-service -f Persister_Service/Dockerfile .

docker network create Week_11_Kafka_Malicious_Text

docker stop persister-service
docker rm persister-service

docker run -d --name persister-service ^
    -e KAFKA_BOOTSTRAP_SERVERS=kafka-broker:9092 ^
    -e COL_NAME_TO_PROCESS=clean_text ^
    -e TOPIC_A=enriched_preprocessed_tweets_antisemitic ^
    -e TOPIC_B=enriched_preprocessed_tweets_not_antisemitic ^
    -e KAFKA_GROUP_ID=group_Persister ^
    -e HOST=mongodb-tweets_db ^
    -e PORT=27017 ^
    -e DB_NAME=tweets_db ^
    --network Week_11_Kafka_Malicious_Text ^
    persister-service:latest


docker login
docker tag persister-service:latest yitzchakdamen/persister-service:latest
docker push yitzchakdamen/persister-service:latest