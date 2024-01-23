import logging


logger = logging.getLogger(__name__)


def func1():
    print('func1')
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
