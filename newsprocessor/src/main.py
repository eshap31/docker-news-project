from redis_integration import RedisConnect
from redis_integration import RedisSubscriber
from mongodb_integration import MongoManager


def main():
    # connect to redis
    connector = RedisConnect()
    connector.initialize_and_connect_to_redis()

    # mongodb integration
    mongo_mgr = MongoManager()
    mongo_mgr.initialize()

    # subscribe and read
    subscriber = RedisSubscriber(connector.redis_cli, mongo_mgr)
    subscriber.subscribe()


if __name__ == "__main__":
    main()
