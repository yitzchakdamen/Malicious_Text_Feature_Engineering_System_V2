
@REM ---- retriever-service ----

cd C:\Users\isaac\source\repos\Malicious_Text_Feature_Engineering_System_V2
docker build -t retriever-service -f Retriever_Service/Dockerfile .

docker network create Week_11_Kafka_Malicious_Text

docker stop retriever-service
docker rm retriever-service

docker run -d --name retriever-service ^
    -e KAFKA_BOOTSTRAP_SERVERS=kafka-broker:9092 ^
    -e USER=IRGC_NEW ^
    -e PASS=iran135 ^
    -e DB_NAME=IranMalDB ^
    -e DNS=cluster0.6ycjkak.mongodb.net/ ^
    -e COLLECTION_NAME=tweets ^
    -e NUM_RECORDS=100 ^
    -e COL_NAME_TO_SORT=CreateDate ^
    -e TIME_SLEEP=60 ^
    --network Week_11_Kafka_Malicious_Text ^
    retriever-service:latest


docker login
docker tag retriever-service:latest yitzchakdamen/retriever-service:latest
docker push yitzchakdamen/retriever-service:latest