from abc import ABC, abstractmethod

class Indexer(ABC):
    @abstractmethod
    def index(self, corpus):
        """Index a corpus of documents."""
        pass

    @abstractmethod
    def update(self, document):
        """Update index with a new document."""
        pass

    @abstractmethod
    def delete(self, document_id):
        """Delete a document from the index."""
        pass
