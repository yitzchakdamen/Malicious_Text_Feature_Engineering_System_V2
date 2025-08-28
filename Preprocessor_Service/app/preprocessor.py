from kafka import KafkaConsumer, KafkaProducer
from Kafka_Tools.kafka_tools import KlakfaTools
from Text_cleaned_and_processed.Text_cleaned_and_processed import TextCleaningProcessing
import logging

logger = logging.getLogger(__name__)

class Preprocessor:
    
    def __init__(self, *topic, bootstrap_servers:str, group_id:str) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.consumer:KafkaConsumer = KlakfaTools.Consumer.get_consumer(topic, bootstrap_servers=bootstrap_servers, group_id=group_id)
        

    def adding_content(self, message, col_name:str, new_col_name):
        message.value[new_col_name] = TextCleaningProcessing.full_processing(message.value[col_name])
        return message

    def system_loop(self, col_name:str, new_col_name):
        """ Listen for messages and process them """
        logger.info("Starting system loop.")
        producer:KafkaProducer = KlakfaTools.Producer.get_producer(self.bootstrap_servers)
        
        for message in self.consumer:
            logger.info(f"Received message: {message.value}: {message.topic}")

            message = self.adding_content(message, col_name, new_col_name)
            KlakfaTools.Producer.publish_message(producer, topic=f"preprocessed_{message.topic[4:]}", message=message.value)
            
            logger.info(f"Published processed message to topic: preprocessed_{message.topic[4:]}")

