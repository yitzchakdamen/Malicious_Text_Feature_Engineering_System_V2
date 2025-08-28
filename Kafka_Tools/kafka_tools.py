from kafka import KafkaConsumer, KafkaProducer
import json
import logging

logger = logging.getLogger(__name__)

class KlakfaTools:
    
    class Producer:
    
        @staticmethod
        def get_producer(bootstrap_servers:str) -> KafkaProducer:
            """Create a Kafka producer."""
            logger.info("Creating producer object ..")
            return KafkaProducer(
                bootstrap_servers=[bootstrap_servers],
                value_serializer=lambda x: json.dumps(x, default=lambda x: str(x)).encode('utf-8')
                )
        
        @staticmethod
        def publish_message(producer:KafkaProducer,  topic, message, key=None):
            """Publish a message to a Kafka topic."""
            logger.info(f"Publish messages with key: {str(key)}, to topic: {str(topic)}")
            producer.send(topic, key=key, value=message)
            producer.flush()
        
        @staticmethod
        def publish_many_by_topics(producer:KafkaProducer, topics:dict[str,str]):
            """Publish data to Kafka."""
            logger.info("Publishing data to Kafka ..")
            
            for topic, messages in topics.items():
                for message in messages:
                    KlakfaTools.Producer.publish_message(producer=producer, topic=topic, key=None, message=message)
    
    class Consumer:
        
        @staticmethod
        def get_consumer(topic, bootstrap_servers:str, group_id:str) -> KafkaConsumer:
            """Create a Kafka consumer."""
            logger.info("Creating Consumer Object ..")
            return KafkaConsumer(
                *topic,
                group_id=group_id,
                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                bootstrap_servers=[bootstrap_servers],
                # consumer_timeout_ms=10000,
                auto_offset_reset='earliest'
            )

        @staticmethod
        def get_consumer_events( *functions, consumer: KafkaConsumer) -> None:
            """Process incoming Kafka messages."""
            logger.info("Listening to Kafka messages ..")
            for message in consumer:
                for function in functions:
                    function(message)