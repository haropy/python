# -- coding: utf-8 --
# 初始化
# 1）直接字符串
from pyquery import PyQuery as pq

doc = pq("<html></html>")
# 2)lxml.etree
from lxml import etree

doc = pq(etree.fromstring("<html></html>"))
# 3)直接传URL
from pyquery import PyQuery as pq

doc = pq('http://www.baidu.com')
# 4)传文件
from pyquery import PyQuery as pq

doc = pq(filename='hello.html')
