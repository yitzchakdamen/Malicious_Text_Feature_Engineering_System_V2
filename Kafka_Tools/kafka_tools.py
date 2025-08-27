from kafka import KafkaConsumer, KafkaProducer
import json
import logging
from config import config

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.getLogger('kafka').setLevel(logging.WARNING)


class KlakfaTools:
    
    class Producer:
    
        @staticmethod
        def get_producer() -> KafkaProducer:
            """Create a Kafka producer."""
            logging.info("Creating producer object ..")
            return KafkaProducer(
                bootstrap_servers=[config.KAFKA_BOOTSTRAP_SERVERS],
                value_serializer=lambda x: json.dumps(x).encode('utf-8')
                )
        
        @staticmethod
        def publish_message(producer:KafkaProducer,  topic, key, message):
            """Publish a message to a Kafka topic."""
            logging.info(f"Publish messages with key: {str(key)}, to topic: {str(topic)}")
            producer.send(topic, key=key, value=message)
            producer.flush()
    
    class Consumer:
        
        @staticmethod
        def get_consumer(topic:str, group_id:str) -> KafkaConsumer:
            """Create a Kafka consumer."""
            logging.info("Creating Consumer Object ..")
            return KafkaConsumer(
                topic,
                group_id=group_id,
                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                bootstrap_servers=[config.KAFKA_BOOTSTRAP_SERVERS],
                # consumer_timeout_ms=10000,
                auto_offset_reset='earliest'
            )

        @staticmethod
        def get_consumer_events(consumer: KafkaConsumer, function) -> None:
            """Process incoming Kafka messages."""
            logging.info("Listening to Kafka messages ..")
            for message in consumer:
                function(message)
                
                