import time
from kafka import KafkaProducer
from Retriever_Service.app.data_loader import DataLoader
from pymongo.command_cursor import CommandCursor
from Kafka_Tools.kafka_tools import KlakfaTools
import logging

logger = logging.getLogger(__name__)

class Retriever:

    def __init__(self, time_sleep:int, loader:DataLoader, bootstrap_servers:str) -> None:
        self.time_sleep = time_sleep
        self.loader = loader
        self.bootstrap_servers = bootstrap_servers

    def retrieve(self, num_records:int, indxs: int, col_name:str) -> CommandCursor:
        """Retrieve data from MongoDB."""
        logger.info("Retrieving data from MongoDB ..")
        pipeline = [
            {"$sort": {col_name: 1}},
            {"$skip": num_records * indxs},
            {"$limit": num_records},
            {"$project": { '_id': 0}}
        ]
        return self.loader.get_data(pipeline)

    def publish(self, producer:KafkaProducer, topics:dict):
        """Publish data to Kafka."""
        logger.info("Publishing data to Kafka ..")
        
        for topic, messages in topics.items():
            for message in messages:
                KlakfaTools.Producer.publish_message(producer=producer, topic=topic, key=None, message=message)
            
    def split_to_topic(self, CommandCursor:list) -> dict:
        antisemitic = [result for result in CommandCursor if result['Antisemitic'] ==1 ]
        not_antisemitic = [result for result in CommandCursor if result['Antisemitic'] ==0 ]
        return  {'raw_tweets_antisemitic':antisemitic, 'raw_tweets_not_antisemitic':not_antisemitic}
    

    def system_loop(self, num_records:int,  col_name:str):
        """System loop for retrieving and publishing data."""
        producer = KlakfaTools.Producer.get_producer(self.bootstrap_servers)
        i = 0
        while True:
            data: CommandCursor = self.retrieve(num_records, i, col_name)
            topics = self.split_to_topic(list(data))
            self.publish(producer, topics)
            time.sleep(self.time_sleep)
            i += 1