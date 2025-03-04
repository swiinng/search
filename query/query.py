from abc import ABC, abstractmethod

class Query(ABC):
    @abstractmethod
    def optimize(self, query):
        """Optimize the query."""
        pass

    @abstractmethod
    def validate(self, query):
        """Validate the query syntax."""
        pass

    @abstractmethod
    def sanitize(self, query):
        """Sanitize input query."""
        pass
    
    # build the query into its class type T build (Query type T)
