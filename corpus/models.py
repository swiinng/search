from dataclasses import dataclass
from enum import Enum

class FileSize(Enum):
    SMALL = 10 * 1024         # < 10 KB
    MEDIUM = 1 * 1024 * 1024  # 1 MB
    LARGE = 5 * 1024 * 1024   # 5 MB
    CUSTOM = None             # User-defined

class FileType(Enum):
    TXT = "txt"
    JSON = "json"
    CSV = "csv"

class CorpusSize(Enum):
    SMALL = 10     # 10 files
    MEDIUM = 100   # 100 files
    LARGE = 1000   # 1000 files
    CUSTOM = None  # User-defined

class Language(Enum):
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    GERMAN = "de"
    CHINESE = "cn"
    JAPANESE = "ja"
    ARABIC = "ar"

@dataclass
class CorpusMetadata:
    file_size: FileSize = FileSize.SMALL
    file_type: FileType
    corpus_size: CorpusSize = CorpusSize.SMALL
    language: Language = Language.ENGLISH
    corpus_store: str