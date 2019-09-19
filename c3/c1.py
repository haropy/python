# -- coding: utf-8 --
# 引入
import requests

r = requests.get('http://cuiqingcai.com')
print type(r)
print r.status_code
print r.encoding
print r.cookies

# 基本请求
r = requests.post('http://httpbin.org/post')
print type(r)
r = requests.put('http://httpbin.org/put')
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')
r = requests.get('http://httpbin.org/get')
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print r.url
