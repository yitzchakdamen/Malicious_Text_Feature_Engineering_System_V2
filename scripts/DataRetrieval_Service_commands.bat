@REM ---- Enricher_Service ----

cd C:\Users\isaac\source\repos\Malicious_Text_Feature_Engineering_System_V2
docker build -t data-retrieval-service -f DataRetrieval_Service/Dockerfile .

docker network create Week_11_Kafka_Malicious_Text

docker stop data-retrieval-service
docker rm data-retrieval-service

docker run -d --name data-retrieval-service ^
    -e HOST=mongodb-tweets_db ^
    -e PORT=27017 ^
    -e DB_NAME=tweets_db ^
    -e USER= ^
    -e PASSWORD= ^
    -e APP_HOST=0.0.0.0 ^
    -e APP_PORT=8000 ^
    --network Week_11_Kafka_Malicious_Text ^
    -p 8000:8000 ^
    data-retrieval-service:latest

docker login
docker tag data-retrieval-service:latest yitzchakdamen/data-retrieval-service:latest
docker push yitzchakdamen/data-retrieval-service:latest
