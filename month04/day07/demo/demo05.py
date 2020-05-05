from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://www.douban.com/')
# 切换到iframe子页面
node = driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')
driver.switch_to.frame(node)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
driver.find_element_by_id('username').send_keys('15851702713')
driver.find_element_by_id('password').send_keys('223751093QWE')
driver.find_element_by_link_text('登录豆瓣').click()
