# -- coding: utf-8 --
import requests

# SSL证书验证
r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
print r.text
