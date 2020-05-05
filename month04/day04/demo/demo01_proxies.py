"""
    收费代理
        建立开放代理的IP池
    思路
        1.
        2.依次对每个代理IP进行测试,能用的保存到文件中
"""
import requests


class ProxyPool:
    def __init__(self):
        self.url = 'http://dev.kdlapi.com/api/'
        self.headers = {}

    def get_html(self):
        html = requests.get(url=self.url, headers=self.headers).text
        proxy_list = html.split('\r\n')
        for proxy in proxy_list:
            if self.check_proxy(proxy):
                pass
        print(html)

    def check_proxy(self, proxy):
        """
        测试ip是否可用
        :param proxy:
        :type proxy:
        :return:
        :rtype:
        """
        test_url = 'http://httpbin.org.get'
        proxies = {
            'http': 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy)
        }
        try:
            res = requests.get(url=test_url, proxies=proxies, headers=self.headers, timeout=2)
            if res.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            return False

    def run(self):
        self.get_html()


if __name__ == '__main__':
    spider = ProxyPool()
    spider.run()
