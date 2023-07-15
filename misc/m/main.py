from pydantic_loggings.rich import Logging

from .c import c as c


logger = Logging().get_logger(
    __name__,
    level='DEBUG',
    force_level=False,
    configure=True,
)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
print(__name__)
