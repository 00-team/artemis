import logging

from .config import BASE_DIR


base_formatter = (
    ('-' * 50) + '\n%(asctime)s\n'
    '%(levelname)s:%(name)s\n'
    '%(message)s\n'
)


def get_logger(name: str, log_file=BASE_DIR / 'bot.log', level=logging.WARNING, formatter=base_formatter):
    formatter = logging.Formatter(formatter)

    handler = logging.FileHandler(log_file, encoding='utf-8')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
