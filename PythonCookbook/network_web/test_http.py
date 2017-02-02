# -*- encoding: utf-8 -*-

import requests


def test_requests():
    resp = requests.head('https://www.python.org')
    status = resp.status_code
    # last_modified = resp.headers['last-modified']
    content_type = resp.headers['content-type']
    content_length = resp.headers['content-length']

    print(status)
    # print(last_modified)
    print(content_type)
    print(content_length)


def test_httpclient():
    from http.client import HTTPConnection
    c = HTTPConnection('www.python.org', 80)
    c.request('HEAD', '/index.html')
    resp = c.getresponse()

    print('Status', resp.status)
    for name, value in resp.headers:
        print(name, value)


if __name__ == '__main__':
    test_httpclient()