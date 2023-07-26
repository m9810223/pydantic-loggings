from pydantic_loggings.rich import Logging


logger = Logging().get_logger(configure=True)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
