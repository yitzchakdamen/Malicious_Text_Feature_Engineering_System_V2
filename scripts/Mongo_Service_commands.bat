docker network create Week_11_Kafka_Malicious_Text

docker stop mongodb-tweets_db
docker rm mongodb-tweets_db

@REM --- kafka ---

@REM --- mongodb ---
docker run -d --name mongodb-tweets_db --network Week_11_Kafka_Malicious_Text  -p 27017:27017 mongodb/mongodb-community-server