import redis
from configurations import LoadEnvVar
from loggers import InitLogger


class RedisConnect:
    def __init__(self):
        self.redis_cli = None
        self.redis_connection = None
        self.env_var_fetcher = LoadEnvVar()

    def initialize_and_connect_to_redis(self):
        self.initialize_redis_cli()
        self.connect_to_redis()
        InitLogger.logger.info(f"Connected to redis service. connection details: {self.redis_connection}")

    def initialize_redis_cli(self):
        host = self.env_var_fetcher.load_env_variable("REDIS_HOST")
        port = self.env_var_fetcher.load_env_variable("REDIS_PORT")
        self.redis_cli = redis.Redis(host=host, port=port, decode_responses=True)
        InitLogger.logger.debug("created redis cli object")

    def connect_to_redis(self):
        self.redis_connection = self.redis_cli.ping()
        InitLogger.logger.debug(f"REDIS connection: {self.redis_connection}")
