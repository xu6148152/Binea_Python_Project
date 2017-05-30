#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from interfaces_protocols.tombola import Tombola


class Fake(Tombola):
    def pick(self):
        return 13


