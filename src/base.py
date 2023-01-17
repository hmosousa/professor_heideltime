import json
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class File:
    def __init__(
            self,
            dct: str,
            text: str,
            language: str,
            **kwargs,
    ):
        self.dct = dct
        self.text = text
        self.language = language
        for key, value in kwargs.items():
            setattr(self, key, value)


class Corpus:
    def __init__(self, path: Path):
        self.path = path
        self._size = None

    def __len__(self) -> int:
        if self._size is None:
            self._size = len(os.listdir(self.path))
        return self._size

    def files(self):
        for filepath in self.path.glob("*.json"):
            content = json.load(filepath.open())
            yield File(**content)
