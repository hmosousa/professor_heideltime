from src.utils import format_bad_date


def test_format_bad_date():
    bad_date = "Sun, 20 Sep 2020 22:47:52 +0200"
    result = format_bad_date(bad_date)
    expected_result = "2020-09-20 22:47:52"
    assert result == expected_result
