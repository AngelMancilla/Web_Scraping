import hashlib
import pymongo
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class MongoPipeline:
    COLLECTION_NAME = 'books'

    def __init__(self, mongo_uri, mongo_db):
        # Initialize MongoDB URI and database name
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        # Load settings from Scrapy crawler
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE")
        )

    def open_spider(self, spider):
        # Open MongoDB connection when spider starts
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        # Close MongoDB connection when spider ends
        self.client.close()

    def process_item(self, item, spider):
        # Compute a unique ID for the item using its URL
        item_id = self.compute_item_id(item)

        # Convert item to a dictionary
        item_dict = ItemAdapter(item).asdict()

        # Upsert the item into the MongoDB collection
        self.db[self.COLLECTION_NAME].update_one(
            filter={"_id": item_id},
            update={"$set": item_dict},
            upsert=True
        )

        return item

    def compute_item_id(self, item):
        # Generate a unique hash ID for the item based on its URL
        url = item["url"]
        return hashlib.sha256(url.encode("utf-8")).hexdigest()

