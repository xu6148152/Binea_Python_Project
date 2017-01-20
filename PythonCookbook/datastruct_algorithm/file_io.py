#! python3
# -*- encoding: utf-8 -*-

def test_open():
    with open('hello.txt', 'wt') as f:
        print('Hello World', file=f)


def test_encode_decode():
    with open('somefile.bin', 'wb') as f:
        text = 'Hello World'
        f.write(text.encode('utf-8'))

    with open('somefile.bin', 'rb') as f:
        data = f.read(16)
        text = data.decode('utf-8')
        print(text)


def test_write_array():
    import array
    nums = array.array('i', [1, 2, 3, 4])
    with open('data.bin', 'wb') as f:
        f.write(nums)

    a = array.array('i', [0, 0, 0, 0, 0, 0])
    with open('data.bin', 'rb') as f:
        f.readinto(a)


def test_xt():
    with open('xt.bin', 'xt') as f:
        f.write('Hello World')


def test_stringio():
    import io
    s = io.StringIO()
    s.write('Hello World\n')
    print(s.getvalue())

