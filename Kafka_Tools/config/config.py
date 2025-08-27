import os
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS","")


logging.info("Configuration Loaded:")
logging.info(f"KAFKA_BOOTSTRAP_SERVERS: {KAFKA_BOOTSTRAP_SERVERS}")