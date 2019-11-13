# -- coding: utf-8 --
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.example.com")
cookie = {'name': 'foo', 'value': 'bar'}
driver.add_cookie(cookie)
driver.get_cookies()