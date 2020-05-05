from selenium import webdriver
import time

class JdSpider(object):
    def __init__(self):
        self.url = 'https://www.jd.com/'
        # 设置无界面模式
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=self.options)

    def get_html(self):
        # get():等页面所有元素加载完成后,才会执行后面的代码
        self.browser.get(self.url)
        # 搜索框 + 搜索按钮
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()

    # 循环体中的函数: 拉进度条,提取数据
    def parse_html(self):
        # 执行js脚本,将进度条拉到最底部
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        # 给页面元素加载预留时间
        time.sleep(3)
        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')

        for li in li_list:
            item = {}
            item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]').text
            item['name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text
            item['commit'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text
            item['shop'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]').text
            print(item)

    def run(self):
        self.get_html()
        while True:
            self.parse_html()
            if self.browser.page_source.find('pn-next disabled') == -1:
                self.browser.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
            else:
                self.browser.quit()
                break

if __name__ == '__main__':
    spider = JdSpider()
    spider.run()