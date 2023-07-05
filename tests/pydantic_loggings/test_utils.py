import logging

import pytest
from pydantic_loggings import utils


@pytest.mark.parametrize(
    ('level', 'name'),
    [
        (logging.CRITICAL, 'CRITICAL'),
        (logging.FATAL, 'CRITICAL'),
        (logging.ERROR, 'ERROR'),
        (logging.WARNING, 'WARNING'),
        (logging.WARN, 'WARN'),
        (logging.INFO, 'INFO'),
        (logging.DEBUG, 'DEBUG'),
        (logging.NOTSET, 'NOTSET'),
    ],
)
def test_get_level_name(level: int, name: str):
    assert logging._levelToName[logging._nameToLevel[name]] == utils.get_level_name(
        level
    )
