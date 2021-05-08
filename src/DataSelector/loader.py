import csv
import json
import os.path


class File:
    def __init__(self, path, delimiter=';'):
        assert os.path.isfile(path)
        assert delimiter is not None
        self.path = path
        self.delimiter = delimiter
        self.raw = self.load()
        self.dict = []

    def readCSV(self) -> None:
        reader = csv.DictReader(self.raw.splitlines(), delimiter=';')
        self.dict = []
        for line in reader:
            self.dict.append(line)

    def readJSON(self) -> None:
        self.dict = json.loads(self.raw)

    def load(self) -> str:
        with open(self.path, 'r') as content:
            raw = content.read()
        return raw

    def getDictList(self) -> list:
        assert len(self.dict) > 0
        return self.dict

    def getRaw(self) -> str:
        assert len(self.raw) > 0
        return self.raw
