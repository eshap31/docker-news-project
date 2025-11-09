import redis
from loggers import InitLogger
from configurations import LoadConfigVariables


class RedisPublisher:
    def __init__(self, redis_cli: redis.Redis):
        self.redis_cli = redis_cli
        self.config_var_loader = LoadConfigVariables()
        self.topic = None

    def publish(self, data):
        self.topic = self.config_var_loader.load_config_variable("redis_topic")
        self.write_to_topic(data)

    def write_to_topic(self, data):
        self.redis_cli.publish(self.topic, data)
        InitLogger.logger.debug(f"published '{data}' to {self.topic}")
