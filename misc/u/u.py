LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            '()': 'uvicorn.logging.DefaultFormatter',
            'fmt': '%(levelprefix)s %(message)s',
            'use_colors': None,
        },
        'access': {
            '()': 'uvicorn.logging.AccessFormatter',
            'fmt': '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',  # noqa: E501
        },
    },
    'handlers': {
        'default': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
        'access': {
            'formatter': 'access',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'uvicorn': {'handlers': ['default'], 'level': 'INFO', 'propagate': False},
        'uvicorn.error': {'level': 'INFO'},
        'uvicorn.access': {'handlers': ['access'], 'level': 'INFO', 'propagate': False},
    },
}
LOGGING_CONFIG = {
    'version': 1,
    'handlers': {
        'rich': {
            '()': 'rich.logging.RichHandler',
            'level': 'DEBUG',
            'omit_repeated_times': False,
            'log_time_format': '%m-%d %H:%M:%S',
            'show_path': False,
            'keywords': [],
        }
    },
    'root': {'level': 'DEBUG', 'handlers': ['rich']},
    # 'loggers': {
    #     'm': {'level': 'INFO'},
    #     # 'm.n': {'level': 'DEBUG'},
    # },
}
