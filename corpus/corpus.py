from abc import ABC, abstractmethod

class Document:
    # maybe change the docid to hash
    def __init__(self, doc_id, content):
        self.doc_id = doc_id
        self.content = content

class Corpus(ABC):
    @abstractmethod
    def generate(self, num_docs, doc_type):
        """Generate a corpus of documents."""
        pass

class CorpusGenerator(Corpus):
    def generate(self, num_docs, doc_type):
        return [Document(i, f"Sample content {i}") for i in range(num_docs)]
