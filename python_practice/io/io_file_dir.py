__author__ = 'xubinggui'

import os

print os.name

print os.uname()

print os.environ

print os.getenv('PATH')

# absolute path
print os.path.abspath('.')

print os.path.join(os.path.abspath('.'), 'testdir')

# os.mkdir(os.path.abspath('.') + '/testdir')
# os.rmdir(os.path.abspath('.') + '/testdir')

print os.path.split(os.path.abspath('.'))

# os.rename(os.path.join(os.path.abspath('.'), 'test.txt'), 'text.py')
# os.rename('text.py', 'dump.txt')

print [x for x in os.listdir('.') if os.path.isdir(x)]
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']