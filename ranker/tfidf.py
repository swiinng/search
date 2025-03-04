from ranker.ranker import Ranker


class TFIDFRanker(Ranker):
    def rank(self, results, query):
        """TF-IDF ranking logic here."""
        return sorted(results, key=lambda x: x[1], reverse=True)