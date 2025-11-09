from newsapi import NewsApiClient
from configurations import LoadEnvVar
from loggers import InitLogger
from configurations import LoadConfigVariables


class NewsApiInit:
    def __init__(self):
        self.newsapi = None
        self.get_env_var = None
        self.api_key = None
        self.query_params_dict = {}
        self.main_url = None

    def initialize(self, var_name):
        InitLogger.logger.debug("starting News Api initialization")
        self.get_env_var = LoadEnvVar()
        self.api_key = self.get_env_var.load_env_variable(var_name)
        self.newsapi = NewsApiClient(api_key=self.api_key)
        self.set_query_params()

    def set_query_params(self):
        config_var_loader = LoadConfigVariables()
        self.query_params_dict = config_var_loader.load_config_variable("query_params")
        self.filter_none_from_query_params()
        InitLogger.logger.debug("loaded query params ")

    def filter_none_from_query_params(self):
        for key, value in self.query_params_dict.items():
            if self.query_params_dict[key] == '':
                self.query_params_dict[key] = None
