from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.command_cursor import CommandCursor

class DataLoader:

    def __init__(self, client_string:str, database:str, collection:str):
        self.client: Database = MongoClient(client_string)[database]
        self.collection: Collection = self.client[collection]

    def retrieve(self,  pipeline:list[dict]) -> CommandCursor:
        """Get data from the specified collection."""
        return self.collection.aggregate(pipeline)

    def close(self):
        """Close the MongoDB client."""
        self.client.close()