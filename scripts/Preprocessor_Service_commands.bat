@REM ---- Preprocessor_Service ----

cd C:\Users\isaac\source\repos\Malicious_Text_Feature_Engineering_System_V2
docker build -t preprocessor-service -f Preprocessor_Service/Dockerfile .

docker network create Week_11_Kafka_Malicious_Text

docker stop preprocessor-service
docker rm preprocessor-service

docker run -d --name preprocessor-service ^
    -e KAFKA_BOOTSTRAP_SERVERS=kafka-broker:9092 ^
    -e COL_NAME_TO_PROCESS=text ^
    -e NEW_COL_NAME=clean_text ^
    -e TOPIC_A=raw_tweets_antisemitic ^
    -e TOPIC_B=raw_tweets_not_antisemitic ^
    -e DNS=cluster0.6ycjkak.mongodb.net/ ^
    -e KAFKA_GROUP_ID=group_Preprocessor ^
    --network Week_11_Kafka_Malicious_Text ^
    preprocessor-service:latest


docker login
docker tag preprocessor-service:latest yitzchakdamen/preprocessor-service:latest
docker push yitzchakdamen/preprocessor-service:latest