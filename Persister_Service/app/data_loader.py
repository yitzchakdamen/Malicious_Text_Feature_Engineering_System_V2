from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.command_cursor import CommandCursor

class DataLoader:

    def __init__(self, client_string:str, database:str):
        self.client: MongoClient = MongoClient(client_string)
        self.db:Database = self.client[database]

    def insert(self,  documents:dict, collection_name:str) -> bool:
        """Insert data into the specified collection."""
        collection: Collection = self.db[collection_name]
        return collection.insert_one(documents).acknowledged

    def close(self):
        """Close the MongoDB client."""
        self.client.close()