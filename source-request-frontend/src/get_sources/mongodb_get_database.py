import pymongo
from configurations import LoadEnvVar


class GetMongoDB:
    def __init__(self, client: pymongo.MongoClient):
        self.client = client
        self.db = None
        self.env_var_loader = LoadEnvVar()

    def get_db(self):
        db_name = self.env_var_loader.load_env_variable("DB_NAME")
        self.db = self.client[db_name]
        print(type(self.db))
