from configurations import LoadEnvVar
from configurations import JsonFileHelper
from loggers import InitLogger


class LoadConfigVariables:
    def __init__(self):
        load_env_var = LoadEnvVar()
        self.config_file_path = load_env_var.load_env_variable("CONFIG_PATH")
        json_file_helper = JsonFileHelper(self.config_file_path)
        self.json_dict = json_file_helper.get_dictionary_from_json_file()

    def load_config_variable(self, variable_name):
        value = self.json_dict[variable_name]
        InitLogger.logger.debug(f"successfully got the value of {variable_name}")
        return value
