# coding=utf-8
import re

__author__ = 'xubinggui'

# 强烈建议使用Python的r前缀，就不用考虑转义的问题了

if(re.match(r'^\d{3}\-\d{3,8}$', '010-12345')):
    print 'ok'
else:
    print 'fail'

print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group(0)
print m.group(1)
print m.group(2)