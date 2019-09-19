# -- coding: utf-8 --
# 代理

import requests

proxies = {
    "https": "http://59.108.125.241"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print r.text

# 也可以通过环境变量HTTP_PROXY 和 HTTPS_PROXY来配置代理
# export HTTP_PROXY = ""
# export HTTPS_PROXY = ""
