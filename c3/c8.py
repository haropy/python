# -- coding: utf-8 --
import requests

# cookies变量来向服务器发送cookie信息
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text
