"""
Utility functions for timing (e.g. tic-yoc functionality)
"""
# Import standard modules
from contextlib import contextmanager
import logging
import time


@contextmanager
def timeit_context(
    name,
    logger=None,
    space="  ",
    logging_level="debug",
    tic=None
):
    """ Time a piece of code

    Example:
    ---------
    with timeit_context("Time to do some random list computation"):
        l = [i**2 for i in range(10000000)]
        del l
    """
    if logger is None:
        logger = logging.getLogger('root')
    tic = time.time() if tic is None else tic
    yield
    elapsedTime = time.time() - tic
    if logging_level == "info":
        # logging.basicConfig(level=logging.INFO)
        logger.info(space + "%s: %.2f sec" % (name, elapsedTime))
    elif logging_level == "debug":
        # logging.basicConfig(level=logging.DEBUG)
        logger.debug(space + "%s: %.2f sec" % (name, elapsedTime))


def setup_logger(name):
    """ Set up custom logger

    References:
    -----------
    https://stackoverflow.com/questions/7621897/python-logging-module-globally
    """
    formatter = logging.Formatter(
        fmt='%(levelname)s:  %(asctime)s - %(module)s - %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S'
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # logger.addHandler(handler)

    return logger
