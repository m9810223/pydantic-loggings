from pprint import pprint as pprint

from pydantic_loggings.base import Logging as BaseLogging
from pydantic_loggings.not_set import Logging as NotSetLogging


if __name__ == '__main__':
    if 0:
        not_set_logger = NotSetLogging(
            _env_file='.env',  # pyright: ignore [reportGeneralTypeIssues]
            _env_file_encoding='utf-8',  # pyright: ignore [reportGeneralTypeIssues]
        ).get_logger()

        not_set_logger.debug('debug')
        not_set_logger.info('info')
        not_set_logger.warning('warning')

    if 0:
        base_logger = BaseLogging(
            # _env_file='.env',  # pyright: ignore [reportGeneralTypeIssues]
        ).get_logger('')

        base_logger.debug('debug')
        base_logger.info('info')
        base_logger.warning('warning')
