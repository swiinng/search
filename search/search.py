from abc import ABC, abstractmethod

class Search(ABC):
    @abstractmethod
    def search(self, index, query, top_k):
        """Perform search on a given index."""
        pass


