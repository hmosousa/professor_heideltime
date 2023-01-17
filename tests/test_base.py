from pathlib import Path

from src.base import Corpus

ROOT_PATH = Path(__file__).parent.parent
PROCESSED_PATH = ROOT_PATH / "data" / "processed"


def test_process_english_corpus():
    path = PROCESSED_PATH / "english"
    corpus = Corpus(path)
    file = next(corpus.files())
    assert file.language == "english"
    assert len(corpus) == 2_688_878


def test_process_french_corpus():
    path = PROCESSED_PATH / "french"
    corpus = Corpus(path)
    file = next(corpus.files())
    assert file.language == "french"
    assert len(corpus) == 41_543


def test_process_german_corpus():
    path = PROCESSED_PATH / "german"
    corpus = Corpus(path)
    file = next(corpus.files())
    assert file.language == "german"
    assert len(corpus) == 174_915


def test_process_italian_corpus():
    path = PROCESSED_PATH / "italian"
    corpus = Corpus(path)
    file = next(corpus.files())
    assert file.language == "italian"
    assert len(corpus) == 10_395


def test_process_portuguese_corpus():
    path = PROCESSED_PATH / "portuguese"
    corpus = Corpus(path)
    file = next(corpus.files())
    assert file.language == "portuguese"
    assert len(corpus) == 38_729


def test_process_spanish_corpus():
    path = PROCESSED_PATH / "spanish"
    corpus = Corpus(path)
    file = next(corpus.files())
    assert file.language == "spanish"
    assert len(corpus) == 432_134
