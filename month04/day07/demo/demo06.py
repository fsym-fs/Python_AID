from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://mail.qq.com/')
# 切换到iframe子页面
# node = driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')
driver.switch_to.frame('login_frame')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
driver.find_element_by_id('u').send_keys('1085414029')
driver.find_element_by_id('p').send_keys('XJBHXYXJYXJFXJL0')
driver.find_element_by_link_text('btn').click()
