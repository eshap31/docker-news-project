from configurations import LoadConfigVariables
from data_filtering import FilterByFieldValue


class SearchManager:
    def __init__(self, mongodb_mgr):
        self.config_var_loader = LoadConfigVariables()
        self.mongodb_mgr = mongodb_mgr

    def get_results(self, requested_value):
        mongo_searcher = self.mongodb_mgr.mongo_searcher
        all_entries = mongo_searcher.search_mongo()
        value_filter = FilterByFieldValue(requested_value, all_entries)
        return value_filter.get_valid_entries()
