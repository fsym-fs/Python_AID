"""
    打开baidu,点击百度一下按钮
"""
from selenium import webdriver

driver = webdriver.Chrome()

# driver.maximize_window()

driver.get(url="http://www.baidu.com/")
# //*[@id="kw"]
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('赵丽颖')
driver.find_element_by_xpath('//*[@id="su"]').click()
# 获取屏幕截图
# driver.save_screenshot('baidu.png')
driver.quit()

