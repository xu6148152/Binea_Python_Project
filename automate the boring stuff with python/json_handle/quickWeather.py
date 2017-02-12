#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import json, requests, sys

# Compute location from command line arguments

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])

# Download the json data from openweathermap.org's api
url = 'http://openweathermap.org/data/2.5/forcecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()
with open('response.txt', 'wb') as writer:
    writer.write(response.text)
# Load json data into a python variable

