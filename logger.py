"""
전역적으로 사용할 logger
"""

import logging

_logger = logging.getLogger('logger')

_logger.setLevel(logging.DEBUG)

_stream_handler = logging.StreamHandler()
_formatter = logging.Formatter('%(process)s %(processName)s %(thread)s %(threadName)s \
%(filename)s line %(lineno)s, %(asctime)s %(levelname)s: %(message)s')
_stream_handler.setFormatter(_formatter)

_logger.addHandler(_stream_handler)

info = _logger.info
debug = _logger.debug
critical = _logger.critical
error = _logger.error
warning = _logger.warning

del _logger, _stream_handler, _formatter
