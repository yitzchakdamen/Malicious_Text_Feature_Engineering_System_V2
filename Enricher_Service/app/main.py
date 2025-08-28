from Preprocessor_Service.app.config import config
from Preprocessor_Service.app.preprocessor import Preprocessor
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
    logging.info("Starting the Preprocessor ..")
    preprocessor = Preprocessor(config.TOPIC_A, config.TOPIC_B, bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS, group_id=config.KAFKA_GROUP_ID)
    preprocessor.system_loop(col_name=config.COL_NAME_TO_PROCESS, new_col_name=config.NEW_COL_NAME)


if __name__ == "__main__":
    main()