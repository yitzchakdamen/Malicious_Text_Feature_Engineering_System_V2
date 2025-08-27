from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.cursor import Cursor

class DataLoader:
    
    def __init__(self, client_string:str, database:str):
        self.client = MongoClient(client_string)[database]

    def get_collection(self, collection:str) -> Collection:
        """Get the specified collection from the database."""
        return self.client[collection]

    def close(self):
        """Close the MongoDB client."""
        self.client.close()
