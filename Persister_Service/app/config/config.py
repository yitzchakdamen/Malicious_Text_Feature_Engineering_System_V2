import os
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)


KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
TOPIC_A = os.getenv("TOPIC_A", "enriched_preprocessed_tweets_antisemitic")
TOPIC_B = os.getenv("TOPIC_B", "enriched_preprocessed_tweets_not_antisemitic")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", f"group_Persister")
HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", "27017")
DB_NAME = os.getenv("DB_NAME", "tweets_db")

logger.info("Configuration Loaded:")
logger.info(f"KAFKA_BOOTSTRAP_SERVERS: {KAFKA_BOOTSTRAP_SERVERS}")
