import csv
import json
import logging
from pathlib import Path
import sys
from typing import Dict

from src.base import File
from src.utils import (
    timestamp_to_date,
    format_bad_date
)

csv.field_size_limit(sys.maxsize // 10)  # fix csv error

logger = logging.getLogger(__name__)

LANGUAGES = [
    "english",
    "french",
    "german",
    "italian",
    "portuguese",
    "spanish",
]


def _read_csv_sequentially(csv_path: Path) -> Dict:
    with open(csv_path, encoding="utf-8") as fin:
        reader = csv.reader(fin)
        for row in reader:
            if reader.line_num == 1:
                header = row
                continue

            yield dict(zip(header, row))


def _read_folder_sequentially(folder_path: Path, extension: str = "") -> Dict:
    filepaths = folder_path.glob(f"*{extension}")
    for filepath in filepaths:
        with open(filepath, encoding="utf-8") as fin:
            yield {"name": filepath.name, "content": fin.read()}


class Corpus:

    def __init__(self, path: Path):
        self.path = path

    def __len__(self):
        count = 0
        for _ in self.files():
            count += 1
        return count

    def files(self):
        yield None


class EnglishCorpus(Corpus):
    language = "english"

    def files(self) -> File:
        rows = _read_csv_sequentially(self.path)
        for content in rows:
            yield File(
                dct=content["date"],
                text=content["article"],
                language=self.language
            )


class FrenchCorpus(Corpus):
    language = "french"

    def files(self) -> File:
        rows = _read_csv_sequentially(self.path)
        for content in rows:
            yield File(
                dct=content["dateDT"],
                text=content["Contenu"],
                language=self.language
            )


class GermanCorpus(Corpus):
    language = "german"

    def files(self) -> File:

        def handle_published_time(value: str):
            if value.isdigit():
                return timestamp_to_date(int(value))
            elif value:
                return format_bad_date(value)
            return ""

        rows = _read_csv_sequentially(self.path)
        for content in rows:
            dct = handle_published_time(content["published"])
            if dct == "":
                msg = f"File {content['title']} has a problem with the published time. " \
                      f"Published time is \'{content['published']}\' while the expected " \
                      f"format is a unix timestamp. Ignoring the file."
                logger.warning(msg)
                continue

            yield File(
                dct=dct,
                text=content["text"],
                language=self.language
            )


class ItalianCorpus(Corpus):
    language = "italian"

    def files(self) -> File:
        rows = _read_csv_sequentially(self.path)
        for content in rows:
            yield File(
                dct=content["publication_date"],
                text=content["text"],
                language=self.language
            )


class PortugueseCorpus(Corpus):
    language = "portuguese"

    def files(self) -> File:
        files = _read_folder_sequentially(self.path, ".json")
        for file in files:
            content = json.loads(file["content"])
            yield File(
                dct=content["data"],
                text=content["texto"].strip(),
                language=self.language
            )


class SpanishCorpus(Corpus):
    language = "spanish"

    def files(self) -> File:
        rows = _read_csv_sequentially(self.path)
        for content in rows:
            yield File(
                dct=content["dct"],
                text=content["text"],
                language=self.language
            )


corpora = [
    EnglishCorpus,
    FrenchCorpus,
    GermanCorpus,
    ItalianCorpus,
    PortugueseCorpus,
    SpanishCorpus,
]
