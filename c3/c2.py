# coding:utf-8
import requests

r = requests.get('a.json')
print r.text
print r.json()


