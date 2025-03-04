from abc import ABC, abstractmethod

class Ranker(ABC):
    @abstractmethod
    def rank(self, results, query):
        """Rank search results based on relevance."""
        pass
