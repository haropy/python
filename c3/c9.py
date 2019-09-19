# -- coding: utf-8 --
import requests

# 会话对象
requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = requests.get("http://httpbin.org/cookies")
print (r.text)
