#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from urllib.request import urlopen
import warnings
import os
import json
from dynamic_attr_and_prop.frozen_json import FronzenJSON

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)


def sort_feed():
    raw_feed = load()
    feed = FronzenJSON(raw_feed)
    sorted(feed.Schedule.keys())
    for key, value in sorted(feed.Schedule.items()):
        print('{:3} {}'.format(len(value), key))


if __name__ == '__main__':
    sort_feed()
