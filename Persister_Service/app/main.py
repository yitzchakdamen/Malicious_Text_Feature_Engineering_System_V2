from Persister_Service.app.config import config
from Persister_Service.app.persister import Persister
from Persister_Service.app.data_loader import DataLoader
import logging
import os
import sys

current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.getLogger('kafka').setLevel(logging.WARNING)

def main():
    """Main entry point for the Persister service."""
    logging.info("Starting the Persister ..")
    
    logging.info("Starting the data retrieval and publishing process ..")
    url:str = f"mongodb://{config.HOST}:{config.PORT}"
    loader = DataLoader(url, config.DB_NAME)
    
    persister = Persister(config.TOPIC_A, config.TOPIC_B, bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS, group_id=config.KAFKA_GROUP_ID)
    persister.system_loop(loader=loader)


if __name__ == "__main__":
    main()