import logging
import sys

def setup_logging():
    """
    Configures the main logger for the application.

    Logs will be printed to the console with a clear format, including
    a timestamp, log level, and message. This provides an informative
    and professional output.
    """
    log_format = logging.Formatter(
        '%(asctime)s - [%(levelname)s] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(log_format)

    logger.addHandler(stream_handler)