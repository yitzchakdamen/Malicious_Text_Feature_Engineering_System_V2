import Retriever_Service.app.config.config as config
from Retriever_Service.app.data_loader import DataLoader
from Retriever_Service.app.retriever import Retriever
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
    logging.info("Starting the data retrieval and publishing process ..")
    url:str = f"mongodb+srv://{config.USER}:{config.PASSWORD}@{config.DNS}"
    loader = DataLoader(url, config.DB_NAME, config.COLLECTION_NAME)

    retriever = Retriever(config.TIME_SLEEP, loader, config.KAFKA_BOOTSTRAP_SERVERS)
    retriever.system_loop(num_records=config.NUM_RECORDS, col_name=config.COL_NAME_TO_SORT)



if __name__ == "__main__":
    main()
    