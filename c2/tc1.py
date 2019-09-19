# -- coding: utf-8 --
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

# 页面操作
# 填充表单
from selenium import webdriver

driver = webdriver.Chrome()
element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_element_by_tag_name("option")
for option in all_options:
    print ("Value is：%s" % option.get_attribute("value"))
    option.click()
# select方法
from selenium.webdriver.support.ui import Select

select = Select(driver.find_element_by_name('name'))
select.select_by_index("index")
select.select_by_visible_text("text")
select.select_by_value("value")

select.deselect_all()  # 取消所有选择
select.all_selected_options  # 获取所有已选项
select.options  # 获取所有可选选项

# 元素拖拽
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains

action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()

# 页面切换
driver.switch_to_window("windowName")

# 获取操作对象
for handle in driver.window_handles:
    driver.switch_to_window(handle)

# 切换frame
driver.switch_to_frame("frameName.0.child")

# 弹窗处理
alert = driver.switch_to_alert()

# 历史记录
driver.forward()
driver.back()

# Cookie处理
# 为页面添加Cookies
driver.get("http://www.example.com")
cookie = {'name': 'foo', 'value': 'bar'}
driver.add_cookie(cookie)
# 获取页面cookie
driver.get_cookies()

# 利用By类来确定那种选择方式
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')

# 显示等待
# 隐式等待是等待特定的时间，显式等待是指定某一条件直到这个条件成立时继续执行。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, "kw"))
finally:
    driver.quit()
