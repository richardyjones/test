from logging import INFO, getLogger
import requests

_logger = getLogger(__name__)
_logger.setLevel(INFO)
try:
    requests.get('/')    
except:
    _logger.exception('test', exc_info=1)
