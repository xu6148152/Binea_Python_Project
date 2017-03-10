# -*-coding:utf8-*-

import requests

payload = {'key1': 'value1', 'key2': 'values'}
r = requests.get('http://www.baidu.com/get', params = payload)

print r.url
# print type(r)
# print r.status_code
# print r.encoding
#
# print r.cookies


