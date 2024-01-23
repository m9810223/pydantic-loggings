from pydantic_loggings.not_set import Logging


logger = Logging().get_logger(configure=True)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
