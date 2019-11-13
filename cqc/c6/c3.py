# -- coding: utf-8 --
from pyquery import PyQuery as pq

p = pq('<p id = "hello" class="hello"></p>')('p')
print p.attr("id")
print p.attr("id", "plop")
print p.attr("id", "hello")
