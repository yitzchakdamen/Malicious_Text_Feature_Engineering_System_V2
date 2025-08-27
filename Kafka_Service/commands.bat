docker network create KafkaNewsStream20

docker stop kafka-broker
docker rm kafka-broker

@REM --- kafka ---

docker run -d --name kafka-broker ^
    --network KafkaNewsStream20 ^
    -p 9092:9092 -p 9093:9093 ^
    -e KAFKA_NODE_ID=1 ^
    -e KAFKA_PROCESS_ROLES=broker,controller ^
    -e KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 ^
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka-broker:9092 ^
    -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER ^
    -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@kafka-broker:9093 ^
    -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 ^
    -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 ^
    -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1 ^
    -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0 ^
    apache/kafka:latest

