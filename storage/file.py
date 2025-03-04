
from storage.storage import Storage


class FileStorage(Storage):
    def save(self, index):
        with open("index.json", "w") as f:
            f.write(str(index))

    def load(self, index_name):
        with open(index_name, "r") as f:
            return eval(f.read())