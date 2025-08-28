
from fastapi import FastAPI
from DataRetrieval_Service.app.data_loader import DataLoader
import logging
import uvicorn
from DataRetrieval_Service.app.config import config 


logging.basicConfig(level=logging.DEBUG)
logging.getLogger('pymongo').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


app = FastAPI()
logging.info("Starting the data retrieval and publishing process ..")
url:str = f"mongodb://{config.HOST}:{config.PORT}"
loader = DataLoader(url, config.DB_NAME)


@app.get("/api/data/{collection_name}")
async def get_data(collection_name: str):
    events = loader.retrieve(collection_name)
    return {
        "status": "success",
        "collection": collection_name,
        "data": events
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.APP_HOST, port=config.APP_PORT)  