import redis.exceptions
from configurations import LoadEnvVar
import pymongo
from pymongo.errors import ConnectionFailure


def main():
    env_var_loader = LoadEnvVar()
    r_cli = redis.Redis(host=env_var_loader.load_env_variable("REDIS_HOST"),
                        port=env_var_loader.load_env_variable("REDIS_PORT"), decode_responses=True)

    db_url = env_var_loader.load_env_variable("DB_URL")

    try:
        if r_cli.ping():
            print("connected to redis")
        mongo_client = pymongo.MongoClient(db_url)
        mongo_client.admin.command('ping')
        print("connected to mongo")
    except redis.exceptions.ConnectionError as e:
        raise e
    except ConnectionFailure as e:
        raise e


if __name__ == "__main__":
    main()
