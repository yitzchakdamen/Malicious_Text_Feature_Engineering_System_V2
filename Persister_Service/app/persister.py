from kafka import KafkaConsumer
from Kafka_Tools.kafka_tools import KlakfaTools
from Persister_Service.app.data_loader import DataLoader
import logging

logger = logging.getLogger(__name__)

class Persister:
    
    def __init__(self, *topic, bootstrap_servers:str, group_id:str) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.consumer:KafkaConsumer = KlakfaTools.Consumer.get_consumer(topic, bootstrap_servers=bootstrap_servers, group_id=group_id)


    def system_loop(self, loader:DataLoader):
        """ Listen for messages and insert them into MongoDB """
        logger.info("Starting system loop.")
        
        for message in self.consumer:
            logger.info(f"Received message: {message.value}: {message.topic}")
            loader.insert(message.value, message.topic[23:])
            logger.info(f" ----- Inserted message into MongoDB ----")