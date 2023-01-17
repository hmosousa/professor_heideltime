import logging
from typing import List

from py_heideltime import heideltime

from src.base import File

logger = logging.getLogger(__name__)


def annotate(file: File) -> List:
    """Weakly label a file with HeidelTime."""
    annotation = heideltime(
        text=file.text,
        language=file.language,
        dct=file.dct[:10]
    )

    if annotation is None:
        msg = f"HeidelTime failed to annotate file with text {file.text}."
        logger.warning(msg)
        return []

    return annotation
