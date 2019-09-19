# -- coding: utf-8 --
import requests

url = 'http://httpbin.org/post'
files = {'file': open('a.txt', 'rb')}
r = requests.post(url, files=files)
print r.text

# 流式上传
with open('massive-body') as f:
    requests.post('http://some.url/streamed', data=f)
