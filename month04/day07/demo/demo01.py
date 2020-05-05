"""
    无界面模式
"""
from selenium import webdriver

# 创建无界面功能对象
options = webdriver.ChromeOptions()

# 添加无界面功能
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

driver.get(url='http://www.baidu.com/')

driver.save_screenshot('baidu.png')
