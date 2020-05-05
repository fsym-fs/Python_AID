from selenium import webdriver

driver = webdriver.Chrome()

driver.get(url="http://www.baidu.com/")

# 获取屏幕截图
# driver.save_screenshot('baidu.png')