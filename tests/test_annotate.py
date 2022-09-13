from src.annotate import annotate
from src.base import File


def test_annotate_english():
    file = File("2012-01-23", "Last year we had fun.", "english")
    result = annotate(file)
    expected_result = [('Last year', (0, 9))]
    assert result == expected_result


def test_annotate_portuguese():
    file = File("2011-01-23", "No próximo ano vai ser divertido.", "portuguese")
    result = annotate(file)
    expected_result = [('próximo', (3, 10))]
    assert result == expected_result
