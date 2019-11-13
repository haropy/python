# -- coding: utf-8 --
import requests
# 获取原始套接字
r = requests.get('https://github.com/timeline.json', stream=True)
print r.raw
print r.raw.read(10)