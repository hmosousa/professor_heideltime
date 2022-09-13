from pathlib import Path

from src.corpora import (
    EnglishCorpus,
    FrenchCorpus,
    GermanCorpus,
    ItalianCorpus,
    PortugueseCorpus,
    SpanishCorpus
)


RAW_PATH = Path("data/raw")


def _test_corpus(corpus):
    file = next(corpus.files())
    assert file.dct
    assert file.text


def test_process_english_corpus():
    path = RAW_PATH / "english" / "data.csv"
    corpus = EnglishCorpus(path)
    _test_corpus(corpus)
    assert corpus.language == "english"


def test_process_french_corpus():
    path = RAW_PATH / "french" / "data.csv"
    corpus = FrenchCorpus(path)
    _test_corpus(corpus)
    assert corpus.language == "french"


def test_process_german_corpus():
    path = RAW_PATH / "german" / "data.csv"
    corpus = GermanCorpus(path)
    _test_corpus(corpus)
    assert corpus.language == "german"


def test_process_italian_corpus():
    path = RAW_PATH / "italian" / "data.csv"
    corpus = ItalianCorpus(path)
    _test_corpus(corpus)
    assert corpus.language == "italian"


def test_process_portuguese_corpus():
    path = RAW_PATH / "portuguese" / "data"
    corpus = PortugueseCorpus(path)
    _test_corpus(corpus)
    assert corpus.language == "portuguese"


def test_process_spanish_corpus():
    path = RAW_PATH / "spanish" / "data.csv"
    corpus = SpanishCorpus(path)
    _test_corpus(corpus)
    assert corpus.language == "spanish"
