import logging
import logging.config

from mod1 import func1
from pydantic_loggings.default import Logging


logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # TODO: modify Handler
    # TODO: export configuration
    Logging(disable_existing_loggers=False).configure()
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    func1()
