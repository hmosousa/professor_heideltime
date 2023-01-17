import argparse


def setup_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--language",
        help="The language of the corpus."
    )

    return parser
