# -- coding: utf-8 --
from bs4 import BeautifulSoup
import lxml

soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print (soup.p.string)
