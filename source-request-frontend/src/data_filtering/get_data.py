import json


class GetDataField:
    def __init__(self):
        self.all_doc_data = None

    def extract_data_as_dictionary(self, iterator):
        self.all_doc_data = []

        for doc in iterator:
            data_str = self.get_data_field(doc)
            data_dict = self.convert_data_to_dictionary(data_str)
            self.all_doc_data.append(data_dict)

    def get_data_field(self, doc):
        return doc['data']

    def convert_data_to_dictionary(self, data):
        d = json.loads(data)
        return d
