"""鼠标事件"""

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url='http://www.baidu.com/')
# 找到设置节点,并移动鼠标

node = driver.find_element_by_xpath('//*[@id="u1"]/a[9]')
# 创建鼠标事件对象
ActionChains(driver).move_to_element(to_element=node).perform()

# 找到高级搜索节点,并点击
driver.find_element_by_link_text('高级搜索').click()