from configurations import LoadConfigVariables


class FilterByFieldValue:
    def __init__(self, value, all_entries):
        self.config_var_loader = LoadConfigVariables()
        self.value = value
        self.field = self.config_var_loader.load_config_variable("field")
        self.entries = all_entries

    def get_valid_entries(self):
        return [entry for entry in self.entries if entry[self.field]['name'] == self.value]
