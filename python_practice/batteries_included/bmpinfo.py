# coding=utf-8
import struct
import sys

__author__ = 'xubinggui'

####################
def isbmp(path):

    f = open(path,'rb')

    b = f.read(30)

    info = struct.unpack('<ccIIIIIIHH',b)

    if info[0]+info[1] == 'BA' or info[0]+info[1] == 'BM':

        print '位图大小：%s,位图颜色：%s' % (info[6]*info[7],info[9])

    else:

        print 'file is not a bmp!'


########################
def bmpinfo(f):

    s = f.read(30)

    info = struct.unpack('<ccIIIIIIHH', s)

    if (info[0] == 'B') and (info[1] == 'M' or info[1] == 'A'):

        print '%s is bitmap, %d x %d, color %d' % (f.name, info[6], info[7], info[9])

    else:

        print '%s not bitmap' % f.name

if __name__ == '__main__':

    import sys

    if len(sys.argv) == 2:

        with open(sys.argv[1], 'rb') as f:

            bmpinfo(f)

    else:

        raise TypeError('takes exactly one argument')