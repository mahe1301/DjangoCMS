import logging
# logger = logging.getLogger(__name__)
logger = logging.getLogger('custom_b2n_logger')

class customlogger:

    def __init__(self):
        self.loggerInfo=logger


# logger.debug()
# logger.info()
# logger.warning()
# logger.error()
# logger.critical()
# There are two other logging calls available:

# logger.log(): Manually emits a logging message with a specific log level.
# logger.exception(): Creates an ERROR level logging message wrapping the current exception stack frame.
