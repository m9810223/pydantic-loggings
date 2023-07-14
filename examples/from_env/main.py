from pathlib import Path

from pydantic_loggings.not_set import Logging


env_file = Path(__file__).parent / '.env'
logger = Logging(_env_file=env_file).get_logger(configure=True)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
