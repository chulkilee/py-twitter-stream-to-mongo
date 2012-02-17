#!/usr/bin/env python
import pymongo

import settings

# mongodb
mongodb_conn = pymongo.Connection()
mongodb_db = mongodb_conn[settings.MONGODB['database']]
mongo_events = mongodb_db[settings.MONGODB['collection']]


def print_count():
    print mongo_events.count()


if __name__ == '__main__':
    print_count()
