import pymongo.synchronous.database

from configurations import LoadEnvVar


class GetMongoCol:
    def __init__(self, db):
        self.db = db
        self.col = None
        self.env_var_loader = LoadEnvVar()

    def get_col(self):
        col_name = self.env_var_loader.load_env_variable("COL_NAME")
        self.col = self.db[col_name]
        print(type(self.col))
