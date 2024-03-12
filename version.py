__version__ = 'Beta_0.1.0'

from yaraforge.metadata import pathnames
from .utils.logger import get_global_logger

logger = get_global_logger(pathnames['logger_dir'])


def get_version():
    """
    Get the version
    :return: The version
    """
    logger.info(f"Getting version {__version__}")
    return __version__
