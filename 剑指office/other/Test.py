'''
    selenium
'''
from selenium import webdriver

driver = webdriver.Chrome("/home/tarena/chromedriver_linux64/chromedriver")
url = "http://www.tmooc.cn/"
path = '/html/body/div[2]/div[2]/div/div[2]/div/div/span'
driver.get(url)
txt = driver.find_element_by_xpath(path)
print(txt.text)

'''
    列表与元组
'''
a = [1, 2.3, 4, 5, 6, 7, 8, 9]
print(a[1:5])
print(type(a))
b = ('s', 'd')
print(type(b))

'''
    GUI
'''
import tkinter

app = tkinter.Tk()
app.mainloop()
