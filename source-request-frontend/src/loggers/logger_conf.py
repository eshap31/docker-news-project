import logging
from configurations import LoadEnvVar


class InitLogger:
    env_loader = LoadEnvVar()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler(env_loader.load_env_variable("LOGGING_PATH"))
    fh.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('- %(levelname)-8s - %(filename)s - %(asctime)s - %(message)s')

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)