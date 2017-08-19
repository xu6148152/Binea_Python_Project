#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from collections import abc
from keyword import iskeyword


class FronzenJSON:
    def __init__(self, mapping):
        self._data = {}
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
                # self._data = dict(mapping)
            self._data[key] = value

    def __getattr__(self, name):
        if hasattr(self._data, name):
            return getattr(self._data, name)
        else:
            # return FronzenJSON.build(self._data[name])
            return FronzenJSON(self._data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableMapping):
            return [cls.build(item) for item in obj]
        else:
            return obj

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls[item] for item in arg]
        else:
            return arg
