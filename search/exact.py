from search.search import Search

class ExactSearch(Search):
    def search(self, index, query, top_k=10):
        return index.search(query)[:top_k]