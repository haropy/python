# -- coding: utf-8 --
# 快速体验
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')

# 模拟提交
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.python.org/')
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print driver.page_source