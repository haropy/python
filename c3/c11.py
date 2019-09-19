# -- coding: utf-8 --
import requests

# 全局变量 取消None
s = requests.session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print r.text
