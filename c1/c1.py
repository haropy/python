# coding:utf-8
# 1）构造Request
import urllib2

response = urllib2.urlopen("https://www.baidu.com")
print response.read()

# 2）POST方式：

import urllib
import urllib2

values = {"username": "haropy", "password": "01TAL0Anet"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()

# 3)GET方式

import urllib
import urllib2

values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()

# 1.设置Headers

import urllib
import urllib2

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username': 'cqc', 'password': 'XXXX'}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()

# 2.Proxy（代理）的设置

import urllib2

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

# 4.使用HTTP的PUT和DELETE方法

import urllib2

uri = ''
request = urllib2.Request(uri, data=data)
request.get_method = lambda: 'PUT'  # or 'DELETE'
response = urllib2.urlopen(request)

# 5.使用DebugLog
import urllib2

httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')

# 1.URLError
import urllib2

requset = urllib2.Request('http://www.xxxxx.com')
try:
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason

# coding:utf-8
import urllib2
import cookielib

# 1)获取Cookie保存到变量
# 声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = ' + item.name
print 'Value = ' + item.value

# 2)保存Cookie到文件
import cookielib
import urllib2

# 设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来创建opener
opener = urllib2.build_opener(handler)
# 创建一个请求
response = opener.open('http://www.baidu.com')
# 保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)

# 3)从文件中获取Cookie并访问
import cookielib
import urllib2

# 创建MozillaCookie实例对象
cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
req = urllib2.Request("http://www.baidu.com")
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()

# 4)利用cookie模拟网站登录
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'username': 'haropy',
    'password': '01TAL0Anet'
})
# 登录csdn
loginUrl = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
# 模拟登录，并把cookie保存到变量
result = opener.open(loginUrl, postdata)
# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
# 利用cookie请求访问到另一个地址
getUrl = 'https://www.csdn.net/'
# 获得结果
result = opener.open(getUrl)
print result.read()
