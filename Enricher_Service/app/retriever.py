from kafka import KafkaConsumer, KafkaProducer
from Kafka_Tools.kafka_tools import KlakfaTools
from Text_cleaned_and_processed.Text_cleaned_and_processed import TextCleaningProcessing
from Enricher_Service.app.analysis import Analysis
import logging

logger = logging.getLogger(__name__)

class Retriever:
    
    def __init__(self, *topic, bootstrap_servers:str, group_id:str) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.consumer:KafkaConsumer = KlakfaTools.Consumer.get_consumer(topic, bootstrap_servers=bootstrap_servers, group_id=group_id)
    

    def adding_content(self, message, col_name:str, new_col_name):
        message.value["sentiment"] = Analysis.sentiment_category(Analysis.analyze_sentiment(message.value[col_name]))
        message.value["weapons_detected"] = Analysis.weapons_detected(message.value["text"])
        message.value["relevant_timestamp"] = Analysis.latest_timestamp(message.value[col_name])
        return message


    def system_loop(self, col_name:str, new_col_name):
        """ Listen for messages and process them """
        logger.info("Starting system loop.")
        producer:KafkaProducer = KlakfaTools.Producer.get_producer(self.bootstrap_servers)
        
        for message in self.consumer:
            logger.info(message)
            logger.info(f"Received message: {message.value}: {message.topic}")
            
            message = self.adding_content(message, col_name, new_col_name)
            KlakfaTools.Producer.publish_message(producer, topic=f"enriched_{message.topic}", message=message.value)

            logger.info(f"Published processed message to topic: enriched_{message.topic}")
