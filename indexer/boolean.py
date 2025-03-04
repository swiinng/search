from indexer.indexer import Indexer


class BooleanIndexer(Indexer):
    def __init__(self):
        self.index = {}

    def index(self, corpus):
        for doc in corpus:
            for word in doc.content.split():
                if word not in self.index:
                    self.index[word] = set()
                self.index[word].add(doc.doc_id)

    def search(self, query):
        return self.index.get(query, set())