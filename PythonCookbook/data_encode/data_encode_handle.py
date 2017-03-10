#! python3
# -*- encoding: utf-8 -*-


def test_stock_csv():
    import csv
    from collections import namedtuple
    with open('AMEX.csv') as f:
        f_csv = csv.reader(f)
        # f_csv = csv.DictReader(f)
        headers = next(f_csv)
        # headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
        print(headers)
        Row = namedtuple('Row', headers)
        print(Row)

        for r in f_csv:
            row = Row(*r)
            print(row)
            # print(r['Name'])

    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007', 'Time': '9:36am', 'Change': -0.18, 'Volume': 181800}]
    with open('stock.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


def test_json_handle():
    import json

    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }

    json_str = json.dumps(data)

    print(json_str)

    data = json.loads(json_str)

    print(data)

    with open('data.json', 'w') as f:
        json.dump(data, f)

    with open('data.json', 'r') as f:
        data = json.load(f)
        print(data)

    # data = json.load(json_str)
    #
    # print(data)

    # from urllib.request import urlopen
    # u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
    # try:
    #     resp = json.loads(u.read().decode('utf-8'))
    # except Exception as e:
    #     print(e)
    #
    # from pprint import pprint
    # pprint(resp)

    s = '{"name": "ACME", "shares": 50, "price": 490.1}'
    from collections import OrderedDict
    data = json.loads(s, object_pairs_hook=OrderedDict)
    print(data)


def test_xml_handle():
    from urllib.request import urlopen
    from xml.etree.ElementTree import parse

    u = urlopen('http://planet.python.org/rss20.xml')
    doc = parse(u)

    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')

        print(title)
        print(date)
        print(link)
        print()


def parse_and_remove(filename, path):
    from xml.etree.ElementTree import iterparse
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


def test_dict_xml():
    s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
    e = dict_to_xml('stock', s)
    from xml.etree.ElementTree import tostring
    print(tostring(e))
    e.set('_id', '1234')
    print(tostring(e))


def dict_to_xml(tag, d):
    from xml.etree.ElementTree import Element
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


def test_binascii():
    s = b'hello'
    import binascii
    h = binascii.b2a_hex(s)
    print(h)
    print(binascii.a2b_hex(h))


def test_base64():
    s = b'hello'
    import base64
    a = base64.b64encode(s)
    print(a)
    print(base64.b64decode(a))


def write_records(records, format, f):
    from struct import Struct
    record_struct = Struct(format)
    for r in records:
        print(r)
        print(*r)
        f.write(record_struct.pack(*r))


def test_struct():
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]
    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)
    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            print(rec)

    with open('data.b', 'rb') as f:
        data = f.read()
    for rec in unpack_records('<idd', data):
        print(rec)


def read_records(format, f):
    from struct import Struct
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


def unpack_records(format, data):
    from struct import Struct
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset) for offset in range(0, len(data), record_struct.size))


def write_polys(filename, polys):
    import struct
    import itertools
    flattened = list(itertools.chain(*polys))
    min_x = min(x for x, y in flattened)
    max_x = max(x for x, y in flattened)
    min_y = min(y for x, y in flattened)
    max_y = max(y for x, y in flattened)
    with open(filename, 'wb') as f:
        f.write(struct.pack('<iddddi', 0x1234, min_x, min_y, max_x, max_y, len(polys)))
        for poly in polys:
            size = len(poly) * struct.calcsize('<dd')
            f.write(struct.pack('<i', size + 4))
            for pt in poly:
                f.write(struct.pack('<dd', *pt))


def read_polys(filename):
    # import struct
    # with open(filename, 'rb') as f:
    #     header = f.read(40)
    #     file_code, min_x, min_y, max_x, max_y, num_polys = struct.unpack('<iddddi', header)
    #     polys = []
    #     for n in range(num_polys):
    #         pbytes, = struct.unpack('<i', f.read(4))
    #         poly = []
    #         for m in range(pbytes // 16):
    #             pt = struct.unpack('<dd', f.read(16))
    #             poly.append(pt)
    #         polys.append(poly)
    # return polys

    polys = []
    with open(filename, 'rb') as f:
        from data_encode.poly_parser import PolyHeader
        from data_encode.poly_parser import SizeRecord
        from data_encode.poly_parser import Point
        phead = PolyHeader.from_file(f)
        for n in range(phead.num_polys):
            rec = SizeRecord.from_file(f, '<i')
            poly = [(p.x, p.y) for p in rec.iter_as(Point)]
            polys.append(poly)
    return polys


def test_poly_handle():
    polys = [
        [(1.0, 2.5), (3.5, 4.0), (2.5, 1.5)],
        [(7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0)],
        [(3.4, 6.3), (1.2, 0.5), (4.6, 9.2)],
    ]
    write_polys('poly.b', polys)
    print(read_polys('poly.b'))

def test_pandas():
    import pandas
    rats = pandas.read_csv('AMEX.csv')
    print(rats)

    print(rats['Symbol'].unique())

    crew_dispatched = rats[rats['Symbol'] == 'FAX']
    print(len(crew_dispatched))


if __name__ == '__main__':
    test_pandas()