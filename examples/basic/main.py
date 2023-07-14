from pydantic_loggings.base import Logging


logger = Logging().get_logger(configure=True)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
