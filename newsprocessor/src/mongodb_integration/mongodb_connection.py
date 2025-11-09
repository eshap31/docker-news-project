from configurations import LoadEnvVar
import pymongo


class MongoConnect:
    def __init__(self):
        self.env_var_loader = LoadEnvVar()
        self.client = None

    def create_connection(self):
        db_url = self.env_var_loader.load_env_variable("DB_URL")
        self.client = pymongo.MongoClient(db_url)
