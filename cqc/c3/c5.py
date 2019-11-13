# -- coding: utf-8 --
import json
import requests

# dumps 表单数据序列化
url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print r.text
