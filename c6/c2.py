# -- coding: utf-8 --
from pyquery import PyQuery as pq

doc = pq(filename='hello.html')
print doc.html()
print type(doc)
li = doc('li')
print type(li)
print li.text()
