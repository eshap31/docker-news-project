import redis
from configurations import LoadConfigVariables
from loggers import InitLogger
from mongodb_integration import MongoManager


class RedisSubscriber:
    def __init__(self, redis_cli: redis.Redis, mongo_mgr: MongoManager):
        self.redis_cli = redis_cli
        self.config_var_loader = LoadConfigVariables()
        self.topic = None
        self.pubsub_reader = None
        self.mongo_mgr = mongo_mgr

    def subscribe(self):
        self.topic = self.config_var_loader.load_config_variable("redis_topic")
        self.pubsub_reader = self.redis_cli.pubsub()
        self.pubsub_reader.subscribe(self.topic)
        self.read_loop()

    def read_loop(self):
        for message in self.pubsub_reader.listen():
            if message["type"] == "message":
                InitLogger.logger.debug(f"received news article: '{message}'")
                print(message)
                self.process_message(message)

    def process_message(self, message):
        self.mongo_mgr.mongo_inserter.insert_to_col(message)

