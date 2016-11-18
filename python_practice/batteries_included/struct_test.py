# coding=utf-8
import struct

__author__ = 'xubinggui'

print struct.pack('>I', 10240099)

print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')