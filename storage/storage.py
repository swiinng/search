from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, index):
        """Save an index."""
        pass

    @abstractmethod
    def load(self, index_name):
        """Load an index."""
        pass
