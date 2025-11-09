from data_filtering import GetDataField


class MongoSearch:
    def __init__(self, col):
        self.col = col

    def search_mongo(self):
        all_entries_iterator = self.col.find()
        data_field_generator = GetDataField()
        data_field_generator.extract_data_as_dictionary(all_entries_iterator)
        all_data = data_field_generator.all_doc_data
        return all_data

    def run_query(self):
        all_entries_iterator = self.col.find()
        return all_entries_iterator
