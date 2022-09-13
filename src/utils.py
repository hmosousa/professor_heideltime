from datetime import datetime
import logging
import shutil
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)


def timestamp_to_date(time: int) -> str:
    """Convert timestamp date to utc date."""
    return datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')


def format_bad_date(date: str) -> str:
    """Format bad dates from german data."""
    return datetime \
        .strptime(date, "%a, %d %b %Y %H:%M:%S %z") \
        .strftime('%Y-%m-%d %H:%M:%S')


def remove_directory(path: str) -> None:
    """Remove the path directory."""
    shutil.rmtree(path)


def annotation_from_xml(xml: str):

    annotation = []

    try:
        root = ET.fromstring(f"<data>{xml}</data>")
    except ET.ParseError:
        logger.warning(f"Was not able to parse file '{xml}'.")
        return []

    idx = 0
    offsets = []
    for element in root.itertext():
        offsets += [(idx, idx + len(element), element)]
        idx += len(element)
    idx += 1  # to take into account the linebreak character

    entities = root.findall("*")
    for entity in entities:
        while True:
            begin, end, text = offsets.pop(0)
            if entity.text == text:
                annotation += [(text, (begin, end))]
                break

    return annotation
