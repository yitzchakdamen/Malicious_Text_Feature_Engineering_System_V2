import os
import time
from pymongo import MongoClient
from kafka import KafkaProducer
import json
from datetime import datetime

class DataLoader:
    def __init__(self):
        mongo_uri = os.getenv("MONGO_URI")
        self.client = MongoClient(mongo_uri)
        self.db = self.client["IranMalDB"]
        self.collection = self.db["tweets"]

        self.producer = KafkaProducer(
            bootstrap_servers=os.getenv("KAFKA_SERVER", "localhost:9092"),
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    def run(self):
        while True:
            docs = self.collection.find().sort("createdate", 1).limit(100)
            for doc in docs:
                topic = "raw_tweets_antisemitic" if doc["antisemietic"] else "raw_tweets_not_antisemitic"
                self.producer.send(topic, {
                    "id": str(doc["_id"]),
                    "createdate": str(doc["createdate"]),
                    "antisemietic": doc["antisemietic"],
                    "text": doc["text"]
                })
            time.sleep(60)

if __name__ == "__main__":
    DataLoader().run()