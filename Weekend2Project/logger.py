import logging

def setup_logger(name, log_file, format, level = logging.INFO):
    formatter = logging.Formatter(format)

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger