#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from configparser import ConfigParser

cfg = ConfigParser()

print(cfg.read('config.ini'))
print(cfg.sections())
print(cfg.get('installation', 'library'))
print(cfg.getboolean('debug', 'log_errors'))

print(cfg.getint('server', 'port'))
print(cfg.getint('server', 'nworkers'))
print(cfg.get('server', 'signature'))

cfg.set('server', 'port', '9000')
cfg.set('debug', 'log_errors', 'False')

import sys

cfg.write(sys.stdout)


