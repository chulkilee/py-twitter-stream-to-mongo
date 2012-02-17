import imp
import logging
from os import path
import sys

TWITTER = {
    'consumer_key': '',
    'consumer_secret': '',
    'oauth_token': '',
    'oauth_token_secret': '',
}

MONGODB = {
    'database': 'twitter_stream',
    'collection': 'events',
}

LOG_FILE = path.join(path.dirname(path.realpath(__file__)), 'dump.log')
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
RECONNECT_SECS = 5

try:
    imp.find_module('local_settings')
except ImportError:
    sys.stderr.write("Error: Cannot find local_settings")
    sys.exit(1)

from local_settings import *
