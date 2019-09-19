# -- coding: utf-8 --
import requests

url = 'http://example.com'
r = requests.get(url)
print r.cookies
print r.cookies['eaxmple_cookie_name']
