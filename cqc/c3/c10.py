# -- coding: utf-8 --
import requests

s = requests.session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print r.text