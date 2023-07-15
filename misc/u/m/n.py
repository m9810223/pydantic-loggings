import logging


logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

logger.debug(f'debug {__name__}')
logger.info(f'info {__name__}')
logger.warning(f'warning {__name__}')
