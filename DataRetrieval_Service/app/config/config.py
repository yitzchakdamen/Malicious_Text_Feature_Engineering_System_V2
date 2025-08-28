import os
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)


HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", "27017")
DB_NAME = os.getenv("DB_NAME", "tweets_db")
USER = os.getenv("USER","")
PASSWORD = os.getenv("PASS","")
APP_HOST = os.getenv("APP_HOST","localhost")
APP_PORT = int(os.getenv("APP_PORT", 8000))


logger.info("Configuration Loaded:")
logger.info(f"USER: {USER}")
logger.info(f"PASSWORD: {PASSWORD}")
logger.info(f"DB_NAME: {DB_NAME}")
logger.info(f"APP_HOST: {APP_HOST}")
logger.info(f"APP_PORT: {APP_PORT}")