import os
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS","")
USER = os.getenv("USER","")
PASSWORD = os.getenv("PASS","")
DB_NAME = os.getenv("DB_NAME","")
DNS = os.getenv("DNS","")
COLLECTION_NAME = os.getenv("COLLECTION_NAME","")
NUM_RECORDS = int(os.getenv("NUM_RECORDS", 100))
COL_NAME_TO_SORT = os.getenv("COL_NAME", "CreateDate")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
TIME_SLEEP = int(os.getenv("TIME_SLEEP", 50))

logger.info("Configuration Loaded:")
logger.info(f"KAFKA_BOOTSTRAP_SERVERS: {KAFKA_BOOTSTRAP_SERVERS}")
logger.info(f"USER: {USER}")
logger.info(f"PASSWORD: {PASSWORD}")
logger.info(f"DB_NAME: {DB_NAME}")
logger.info(f"DNS: {DNS}")