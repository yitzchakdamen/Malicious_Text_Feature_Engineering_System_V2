from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


class DataLoader:

    def __init__(self, client_string:str, database:str):
        self.client: Database = MongoClient(client_string)[database]

    def retrieve(self,  collection_name:str) -> list[dict]:
        """Retrieve data from the specified collection."""
        collection: Collection = self.client[collection_name]
        return list(collection.find({}, {'_id': 0}))

    def close(self):
        """Close the MongoDB client."""
        self.client.close()