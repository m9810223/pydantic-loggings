import logging.config

from u import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)

import logging


logger = logging.getLogger(__name__)
