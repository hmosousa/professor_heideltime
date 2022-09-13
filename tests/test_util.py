from src.utils import format_bad_date, annotation_from_xml


def test_format_bad_date():
    bad_date = "Sun, 20 Sep 2020 22:47:52 +0200"
    result = format_bad_date(bad_date)
    expected_result = "2020-09-20 22:47:52"
    assert result == expected_result


def test_annotation_from_xml():
    xml = 'Was not able to start the diet <TIMEX3 tid="t1" type="DATE" value="2003-11-05">today</TIMEX3>. ' \
          '<TIMEX3 tid="t2" type="DATE" value="2003-11-06">Tomorrow</TIMEX3> is the day.'
    result = annotation_from_xml(xml)
    expected_result = [("today", (31, 36)), ("Tomorrow", (38, 46))]
    assert result == expected_result
