import json
from loggers import InitLogger

class JsonFileHelper:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_dictionary_from_json_file(self):
        json_data = self.get_json_file_contents()

        InitLogger.logger.debug(f"successfully got contents of json file: {self.file_path}")
        return json_data

    def get_json_file_contents(self):
        with open(self.file_path, 'r') as file:
            json_str = json.load(file)

        InitLogger.logger.debug(f"Successfully opened json file - {self.file_path}")
        return json_str
