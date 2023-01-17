import json
import logging.config
from pathlib import Path

from src.annotate import annotate
from src.base import Corpus
from src.cli import setup_parser
from src.data import process
from src.meta import LANGUAGES

ROOT_PATH = Path(__file__).parent.parent
DATA_PATH = ROOT_PATH / "data"

logging.config.fileConfig(ROOT_PATH / "logging.conf")
logger = logging.getLogger(__name__)


def main() -> None:
    parser = setup_parser()
    args = parser.parse_args()

    if args.language not in LANGUAGES:
        msg = f"There is no corpus for the provided language '{args.language}'." \
              f"The supported languages are the following: {LANGUAGES}."
        logger.error(msg)
        return

    raw_data_path = DATA_PATH / "raw" / args.language
    if not raw_data_path.exists():
        msg = f"Folder '{raw_data_path}' does not exist. " \
              f"Please follow the instruction in the README.md file to download the raw data."
        logger.error(msg)
        return

    processed_data_path = DATA_PATH / "processed" / args.language
    if not processed_data_path.exists():
        logger.info(f"Processing raw data.")
        process(args.language)

    logger.info(f"Making annotations for language {args.language}.")
    corpus = Corpus(processed_data_path)

    output_path = DATA_PATH / "annotated" / args.language
    output_path.mkdir(exist_ok=True, parents=True)

    # check if the output dir has annotated files.
    processed_file_idxs = [int(file.name.strip(".json")) for file in output_path.glob("*.json")]
    processed_file_idxs += [0]  # guard in case no file has been processed

    processed_file_idx = max(processed_file_idxs)
    for file_idx, file in enumerate(corpus.files()):

        if file_idx + 1 < processed_file_idx:  # file was already annotated.
            continue

        logger.info(f"\tAnnotating file {file_idx}/{len(corpus)}.")

        try:
            annotation = annotate(file)
        except IndexError:
            logger.warning(f"There was a problem in the annotation of file with id {file_idx}.")
            continue

        if not annotation:
            logger.info("\tDid not find any timexs for this file.")
            continue

        result = {
            "dct": file.dct,
            "text": file.text,
            "timexs": annotation
        }

        filepath = output_path / f"{file_idx:012}.json"
        with open(filepath, "w", encoding="utf-8") as fout:
            json.dump(result, fout, indent=4, ensure_ascii=True)


if __name__ == "__main__":
    main()
