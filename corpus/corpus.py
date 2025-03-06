from abc import ABC, abstractmethod

from corpus.models import CorpusMetadata

class Corpus(ABC):
    @abstractmethod
    def generate(self, corpus_metadata: CorpusMetadata):
        """Generate a corpus of documents."""
        pass
