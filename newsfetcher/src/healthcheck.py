import redis.exceptions
from configurations import LoadEnvVar


def main():
    env_var_loader = LoadEnvVar()
    r_cli = redis.Redis(host=env_var_loader.load_env_variable("REDIS_HOST"),
                        port=env_var_loader.load_env_variable("REDIS_PORT"), decode_responses=True)

    try:
        if r_cli.ping():
            print("connected")
    except redis.exceptions.ConnectionError as e:
        raise e


if __name__ == "__main__":
    main()
