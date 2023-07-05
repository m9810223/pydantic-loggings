from pydantic_loggings.base import Logging


logger = Logging().configure_and_get_logger()

logger.debug('debug')
logger.info('info')
logger.warning('warning')
