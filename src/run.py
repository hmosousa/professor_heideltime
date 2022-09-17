import json
import logging.config
from pathlib import Path

from src.annotate import annotate
from src.cli import setup_parser
from src.corpora import corpora, LANGUAGES

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


def main() -> None:
    parser = setup_parser()
    args = parser.parse_args()

    if args.language not in LANGUAGES:
        msg = f"There is no corpus for the provided language '{args.language}'." \
              f"The supported languages are the following: {LANGUAGES}."
        logger.error(msg)
        return

    data_path = Path(args.data_path)
    if not data_path.exists():
        msg = f"Folder '{data_path}' does not exist. " \
              f"Please follow the instruction in the README.md file."
        logger.error(msg)
        return

    logger.info(f"Making annotations for language {args.language}.")

    [corpus] = [corpus(data_path) for corpus in corpora if corpus.language == args.language]

    output_path = Path(args.output_path)
    output_path.mkdir(exist_ok=True)

    # check if the output dir has annotated files.
    if list(output_path.glob("*.json")):
        processed_file_idx = max(
            int(file.name.strip(".json"))
            for file in output_path.glob("*.json")
        )
    else:
        processed_file_idx = 0

    for file_idx, file in enumerate(corpus.files()):

        if file_idx + 1 < processed_file_idx:  # file was already annotated.
            continue

        if int(args.n_files_annotate) <= file_idx + 1:  # achieved the  annotation budget.
            break

        logger.info(f"\tAnnotating file {file_idx}/{args.n_files_annotate}.")

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
