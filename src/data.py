import csv
import json
import logging
import sys
from pathlib import Path
from typing import Dict

from src.utils import format_bad_date, timestamp_to_date

csv.field_size_limit(sys.maxsize // 10)  # fix csv error

logger = logging.getLogger(__name__)

ROOT_PATH = Path(__file__).parent.parent
RAW_DATA_PATH = ROOT_PATH / "data" / "raw"
PROCESSED_DATA_PATH = ROOT_PATH / "data" / "processed"


def _read_csv_sequentially(csv_path: Path) -> Dict:
    with open(csv_path, encoding="utf-8") as fin:
        reader = csv.reader(fin)
        for row in reader:
            if reader.line_num == 1:
                header = row
                continue

            yield dict(zip(header, row))


def _read_folder_sequentially(folder_path: Path) -> Dict:
    filepaths = folder_path.glob(f"*.json")
    for filepath in filepaths:
        content = json.load(filepath.open())
        content["name"] = filepath.name
        yield content


def _process_english_corpus():
    language = "english"
    logger.info(f"Processing {language} files.")
    (PROCESSED_DATA_PATH / language).mkdir(parents=True, exist_ok=True)
    idx = 0
    rows = _read_csv_sequentially(RAW_DATA_PATH / language / "data.csv")
    for content in rows:
        content["dct"] = content.pop("date")
        content["text"] = content.pop("article").strip()
        content["language"] = language

        processed_file_path = PROCESSED_DATA_PATH / language / f"{idx:08}.json"
        json.dump(content, processed_file_path.open("w"), indent=4)
        idx += 1


def _process_french_corpus():
    language = "french"
    logger.info(f"Processing {language} files.")
    (PROCESSED_DATA_PATH / language).mkdir(parents=True, exist_ok=True)
    idx = 0
    rows = _read_csv_sequentially(RAW_DATA_PATH / language / "data.csv")
    for content in rows:
        content["dct"] = content.pop("dateDT")
        content["text"] = content.pop("Contenu").strip()
        content["language"] = language

        processed_file_path = PROCESSED_DATA_PATH / language / f"{idx:08}.json"
        json.dump(content, processed_file_path.open("w"), indent=4)
        idx += 1


def _process_german_corpus():
    def handle_published_time(value: str) -> str:
        if value.isdigit():
            return timestamp_to_date(int(value))
        elif value:
            return format_bad_date(value)
        return ""

    language = "german"
    logger.info(f"Processing {language} files.")
    (PROCESSED_DATA_PATH / language).mkdir(parents=True, exist_ok=True)
    idx = 0
    rows = _read_csv_sequentially(RAW_DATA_PATH / language / "data.csv")
    for content in rows:
        dct = handle_published_time(content["published"])
        if dct == "":
            msg = f"File {content['title']} has a problem with the published time. " \
                  f"Published time is \'{content['published']}\' while the expected " \
                  f"format is a unix timestamp. Ignoring the file."
            logger.warning(msg)
            continue

        content["dct"] = dct
        content["text"] = content.pop("text").strip()
        content["language"] = language

        processed_file_path = PROCESSED_DATA_PATH / language / f"{idx:08}.json"
        json.dump(content, processed_file_path.open("w"), indent=4)
        idx += 1


def _process_italian_corpus():
    language = "italian"
    logger.info(f"Processing {language} files.")
    (PROCESSED_DATA_PATH / language).mkdir(parents=True, exist_ok=True)
    idx = 0
    rows = _read_csv_sequentially(RAW_DATA_PATH / language / "data.csv")
    for content in rows:
        content["dct"] = content.pop("publication_date")
        content["text"] = content.pop("text").strip()
        content["language"] = language

        processed_file_path = PROCESSED_DATA_PATH / language / f"{idx:08}.json"
        json.dump(content, processed_file_path.open("w"), indent=4)
        idx += 1


def _process_portuguese_corpus():
    language = "portuguese"
    logger.info(f"Processing {language} files.")
    (PROCESSED_DATA_PATH / language).mkdir(parents=True, exist_ok=True)
    idx = 0
    rows = _read_folder_sequentially(RAW_DATA_PATH / language / "data")
    for content in rows:
        content["dct"] = content.pop("data")
        content["text"] = content.pop("texto").strip()
        content["language"] = language

        processed_file_path = PROCESSED_DATA_PATH / language / f"{idx:08}.json"
        json.dump(content, processed_file_path.open("w"), indent=4)
        idx += 1


def _process_spanish_corpus():
    language = "spanish"
    logger.info(f"Processing {language} files.")
    (PROCESSED_DATA_PATH / language).mkdir(parents=True, exist_ok=True)
    idx = 0
    rows = _read_csv_sequentially(RAW_DATA_PATH / language / "data.csv")
    for content in rows:
        if "dct" not in content:
            print(content)
            continue

        content["dct"] = content.pop("dct")
        content["text"] = content.pop("text").strip()
        content["language"] = language

        processed_file_path = PROCESSED_DATA_PATH / language / f"{idx:08}.json"
        json.dump(content, processed_file_path.open("w"), indent=4)
        idx += 1


def process(language: str) -> None:
    match language.lower():
        case "english":
            _process_english_corpus()
        case "french":
            _process_french_corpus()
        case "german":
            _process_german_corpus()
        case "italian":
            _process_italian_corpus()
        case "portuguese":
            _process_portuguese_corpus()
        case "spanish":
            _process_spanish_corpus()
