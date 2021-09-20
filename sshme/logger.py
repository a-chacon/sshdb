import os
import logging
from .constants import (
    CONFIG_DIR
)

def get_logger():
    """
    Create the logger.
    """
    # Gets or creates a logger
    logger = logging.getLogger(__name__)

    # set log level
    logger.setLevel(logging.DEBUG)

    LOGFILE = os.path.join(CONFIG_DIR, "ssh-manager.log")

    # TBD, maybe /var/log is the better option
    if not os.path.isdir(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)

    # define file handler and set formatter
    file_handler = logging.FileHandler(CONFIG_DIR + '/ssh-manager.log')
    formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)

    # add file handler to logger
    logger.addHandler(file_handler)

    return logger

logger = get_logger()
