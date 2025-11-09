from loggers import InitLogger


class InsertToCol:
    def __init__(self, col):
        self.col = col

    def insert_to_col(self, document):
        doc_id = self.col.insert_one(document)
        InitLogger.logger.info(f"added document to collection, the id is: {doc_id}")
