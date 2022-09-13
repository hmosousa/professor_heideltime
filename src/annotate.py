import logging
from typing import List

from py_heideltime import py_heideltime

from src.base import File
from src.utils import annotation_from_xml

logger = logging.getLogger(__name__)


def annotate(file: File) -> List:
    """Weakly label a file with HeidelTime."""
    prediction = py_heideltime(
        text=file.text,
        language=file.language,
        document_creation_time=file.dct[:10]
    )

    if prediction is None:
        msg = f"HeidelTime failed to annotate file with text {file.text}."
        logger.warning(msg)
        return []

    _, _, xml, _ = prediction
    return annotation_from_xml(xml)
