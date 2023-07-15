from pydantic_loggings.rich import Logging


logger = Logging().get_logger(
    __name__,
    level='DEBUG',
    # configure=True,
    # force_level=True,
)


logger.debug('debug')
logger.info('info')
logger.warning('warning')
print(__name__)
