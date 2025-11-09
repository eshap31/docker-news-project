import os
from dotenv import load_dotenv


class LoadEnvVar:
    def load_env_variable(self, variable_name):
        load_dotenv()
        return_value = os.getenv(variable_name)
        return return_value

