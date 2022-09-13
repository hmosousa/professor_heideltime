import argparse


def setup_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--data_path",
        help="The path with the data to read."
    )

    parser.add_argument(
        "--language",
        help="The language of the corpus."
    )

    parser.add_argument(
        "--n_files_annotate",
        default=1_000,
        help="The number of files to annotate."
    )

    parser.add_argument(
        "--output_path",
        help="The folder path to store the annotated files."
    )

    return parser
