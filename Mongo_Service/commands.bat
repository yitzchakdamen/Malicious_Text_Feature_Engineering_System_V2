docker network create KafkaNewsStream20

docker stop mongodb-tweets_db
docker rm mongodb-tweets_db

@REM --- kafka ---

@REM --- mongodb ---
docker run -d --name mongodb-tweets_db --network KafkaNewsStream20  -p 27017:27017 mongodb/mongodb-community-server