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
