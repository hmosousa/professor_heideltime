import csv
import logging
from pathlib import Path
import sys
from typing import Dict

from src.base import File
from src.utils import timestamp_to_date, format_bad_date

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


def _read_folder_sequentially(folder_path: Path) -> Dict:
    filepaths = folder_path.glob("*.txt")
    for filepath in filepaths:
        with open(filepath, encoding="utf-8") as fin:
            yield {"name": filepath.name, "content": fin.read()}


class EnglishCorpus:
    def __init__(self, path: Path):
        self.path = path
        self.language = "english"

    def files(self) -> File:
        rows = _read_csv_sequentially(self.path)
        for content in rows:
            yield File(
                dct=content["date"],
                text=content["article"],
                language=self.language
            )


class FrenchCorpus:
    def __init__(self, path: Path):
        self.path = path
        self.language = "french"

    def files(self) -> File:
        rows = _read_csv_sequentially(self.path)
        for content in rows:
            yield File(
                dct=content["dateDT"],
                text=content["Contenu"],
                language=self.language
            )


class GermanCorpus:
    def __init__(self, path: Path):
        self.path = path
        self.language = "german"

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


class ItalianCorpus:
    def __init__(self, path: Path):
        self.path = path
        self.language = "italian"

    def files(self) -> File:
        rows = _read_csv_sequentially(self.path)
        for content in rows:
            yield File(
                dct=content["publication_date"],
                text=content["text"],
                language=self.language
            )


class PortugueseCorpus:
    def __init__(self, path: Path):
        self.path = path
        self.language = "portuguese"

    def files(self) -> File:
        files = _read_folder_sequentially(self.path)
        for file in files:
            year, month, day = file["name"][:10].split("_")
            dct = f"{year}-{month}-{day}"
            yield File(
                dct=dct,
                text=file["content"].strip(),
                language=self.language
            )


class SpanishCorpus:
    def __init__(self, path: Path):
        self.path = path
        self.language = "spanish"

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
