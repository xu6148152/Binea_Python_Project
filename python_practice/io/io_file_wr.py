import codecs
__author__ = 'xubinggui'

try:
    f = open('/Users/xubinggui/Downloads/test.txt', 'r')
    print f.read()

finally:
    if f:
        f.close()

with open('/Users/xubinggui/Downloads/test.txt', 'rb') as f:
    print f.read().decode('UTF-8')

with codecs.open('/Users/xubinggui/Downloads/test.txt', 'r') as f:
    print f.read()

with codecs.open('/Users/xubinggui/Downloads/test.txt', 'w') as f:
    f.write('hello world')