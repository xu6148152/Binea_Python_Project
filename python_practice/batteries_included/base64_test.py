# coding=utf-8
import base64

__author__ = 'xubinggui'

print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')

print base64.b64encode('i\xb7\x1d\xfb\xef\xff')

print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')

print base64.urlsafe_b64decode('abcd--__')

def safe_b64decode(s):

    remainder = len(s) % 4

    if remainder: s += '=' * (4 - remainder)

    return base64.b64decode(s)

print base64.b64decode('YWJjZA==')
print safe_b64decode('YWJjZA')