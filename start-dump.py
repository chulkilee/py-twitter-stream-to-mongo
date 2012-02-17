#!/usr/bin/env python
import logging
import time
import sys

import pymongo
import twitter

import settings

stream = twitter.TwitterStream(secure=True,
       auth=twitter.oauth.OAuth(
           token=settings.TWITTER['oauth_token'],
           token_secret=settings.TWITTER['oauth_token_secret'],
           consumer_key=settings.TWITTER['consumer_key'],
           consumer_secret=settings.TWITTER['consumer_secret']))

# mongodb
mongodb_conn = pymongo.Connection()
mongodb_db = mongodb_conn[settings.MONGODB['database']]
mongo_events = mongodb_db[settings.MONGODB['collection']]

# logger
logging.basicConfig(filename=settings.LOG_FILE, level=settings.LOG_LEVEL,
    format=settings.LOG_FORMAT)


def dump():
    while True:
        try:
            iterator = stream.statuses.sample()
            for event in iterator:
                mongo_events.insert(event)
        except Exception as e:
            logging.warn(type(e))
            logging.warn(str(e))
            time.sleep(settings.RECONNECT_SECS)


if __name__ == '__main__':
    dump()
