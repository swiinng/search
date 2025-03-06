from typing import Dict
from faker import Faker

from corpus.corpus import Corpus
from corpus.models import CorpusMetadata, Language


class TextCorpus(Corpus):
    _fakers: Dict[Language, Faker] = {}

    def generate(self, corpus_metadata: CorpusMetadata):
        if corpus_metadata.language not in self._fakers:
            self._fakers[corpus_metadata.language] = Faker(locale=corpus_metadata.language)