import os
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)


KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
COL_NAME_TO_PROCESS = os.getenv("COL_NAME_TO_PROCESS", "text")
NEW_COL_NAME = os.getenv("NEW_COL_NAME", "clean_text")
TOPIC_A = os.getenv("TOPIC_A", "raw_tweets_antisemitic")
TOPIC_B = os.getenv("TOPIC_B", "raw_tweets_not_antisemitic")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", f"group_Preprocessor")

logger.info("Configuration Loaded:")
logger.info(f"KAFKA_BOOTSTRAP_SERVERS: {KAFKA_BOOTSTRAP_SERVERS}")
