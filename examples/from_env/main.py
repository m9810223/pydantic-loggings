from pathlib import Path

from pydantic_loggings.not_set import Logging


env_file = Path(__file__).parent / '.env'
logger = Logging(
    _env_file=env_file  # pyright: ignore [reportGeneralTypeIssues]
).get_logger()

logger.debug('debug')
logger.info('info')
logger.warning('warning')
