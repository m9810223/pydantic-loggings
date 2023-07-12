from pydantic_loggings.not_set import Logging


logger = Logging().get_logger()

logger.debug('debug')
logger.info('info')
logger.warning('warning')
