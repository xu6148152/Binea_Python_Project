# !python3
import re

def test_re_split():
    line = 'asdf fjdk; dfjkaf, fdjksf, jdksf, foo'

    print(re.split(r'[;,\s]\s*', line))

    fields = re.split(r'(;|,|\s)\s*', line)
    print(fields)

    values = fields[::2]
    print(values)
    delimiter = fields[1::2] + ['']
    print(delimiter)

    print(re.split(r'(?:,|;|\s)\s*', line))


def test_start_with():
    filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
    print([name for name in filenames if name.endswith(('.c', '.h'))])

    print(any(name.endswith('.py')) for name in filenames)

def test_fnmatch():
    from fnmatch import fnmatch, fnmatchcase
    print(fnmatch('foo.txt', '*.txt'))
    print(fnmatchcase('foo.txt', '*.TXT'))


def test_str_match():
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'

    m = datepat.match(text1)
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.groups())

    text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
    print(datepat.findall(text))

def test_str_replace():
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(datepat.sub(r'\3-\1-\2', text))

    print(datepat.sub(change_date, text))


def change_date(m):
    from calendar import month_abbr
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


def test_unicode():
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    s3 = 'Spicy Jalape\xf1o'

    import unicodedata
    # NFC表示字符整体组成
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    # NFD表示字符分解多个表示
    t3 = unicodedata.normalize('NFD', s3)
    print(t1)
    print(t2)
    print(t3)


def test_strip():
    s = ' Hello world \n'
    print(s.strip())
    t = '--------------hello========'
    print(t.strip('-='))


def test_translate():
    import unicodedata
    import sys
    digitmap = {c: ord('0') + unicodedata.digit(chr(c))
                for c in range(sys.maxunicode)
                if unicodedata.category(chr(c)) == 'Nd'}
    x = '\u0661\u0662\u0663'
    print(x.translate(digitmap))


def test_just():
    text = 'Hello World'
    print(text.ljust(20, '='))
    print(text.rjust(20))
    print(text.center(20, '*'))

    print(format(text, '=>20'))
    print(format(text, '*^20'))

    print('{:>10s} {:>10s}'.format('Hello', 'World'))


def test_join():
    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print(' '.join(parts))
    print(','.join(parts))
    print(''.join(parts))

    a = 'Is Chicago'
    b = 'Not Chicago'
    c = 'None'
    print(a + ' ' + b)
    print('Hello' 'World')

    date = ['ACME', 50, 91.1]
    print(','.join(str(d) for d in date))
    print(a, b, c, sep=':')


def test_format():
    s = '{name} has {n} message'
    print(s.format(name='Guido', n=37))

    name = 'Guido'
    # n = 37
    # print(s.format_map(vars()))

    print(s.format_map(SafeSub(vars())))

    print(sub('Hello {name}'))
    print(sub('You have {n} messages.'))


class SafeSub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


def sub(text):
    import sys
    return text.format_map(SafeSub(sys._getframe(1).f_locals))


def test_textwrap():
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, " \
        "the eyes, not around the eyes, don't look around the eyes," \
        "look into my eyes, you're under"
    import textwrap
    print(textwrap.fill(s, 40, initial_indent='  '))
    print(textwrap.fill(s, 40, subsequent_indent='  '))

    import os
    # os.get_terminal_size().columns


def generate_tokens(pat, text):
    from collections import namedtuple
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


def test_bin_text():
    a = b'Hello World'
    print(a)
    print(a[0])
    print(a.decode('ascii'))

if __name__ == '__main__':
    test_bin_text()