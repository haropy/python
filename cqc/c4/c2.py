# -- coding: utf-8 --
from bs4 import BeautifulSoup

data_soup = BeautifulSoup('div data-foo = "value">foo!</div>', 'html.parser')
print data_soup.find_all(data_foo="value")
