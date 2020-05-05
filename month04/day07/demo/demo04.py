from selenium import webdriver
import redis
from hashlib import md5
class GovSpider(object):
    def __init__(self):
        # 设置无界面
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # 添加参数
        # self.browser = webdriver.Chrome(options=options)
        self.browser = webdriver.Chrome()
        self.one_url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        #


    def get_incr_url(self):
        self.browser.get(self.one_url)
        # 提取最新链接节点对象并点击
        self.browser.find_element_by_xpath('//td[@class="arlisttd"]/a[contains(@title,"代码")]').click()
        # 切换句柄
        all_handlers = self.browser.window_handles
        self.browser.switch_to.window(all_handlers[1])
        self.get_data()

    def get_data(self):
        tr_list = self.browser.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            print(name,code)

    def run(self):
        self.get_incr_url()
        self.browser.quit()

if __name__ == '__main__':
  spider = GovSpider()
  spider.run()