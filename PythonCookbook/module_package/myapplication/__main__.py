# -*- encoding: utf-8 -*-
# from ..myapplication import bar
# from ..myapplication import grok
# from ..myapplication import spam
import sys

from module_package.myapplication import bar

sys.path.append(['bar.py', 'grok.py', 'spam.py'])
if __name__ == '__main__':
    print('Hello world')
    bar.bar()
    # grok.grok()
    # spam.spam()
