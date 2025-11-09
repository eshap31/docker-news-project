from get_sources import *


class MongoManager:
    def __init__(self):
        self.mongo_connect = MongoConnect()
        self.mongo_get_db = None
        self.mongo_get_col = None
        self.mongo_searcher = None

    def initialize(self):
        self.mongo_connect.create_connection()
        self.mongo_get_db = GetMongoDB(self.mongo_connect.client)
        self.mongo_get_db.get_db()
        self.mongo_get_col = GetMongoCol(self.mongo_get_db.db)
        self.mongo_get_col.get_col()
        self.mongo_searcher = MongoSearch(self.mongo_get_col.col)
