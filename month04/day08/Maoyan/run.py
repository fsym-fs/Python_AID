from scrapy import cmdline


"""
    1、下载器多线程、爬虫文件协程，所以所抓数据无序很正常(但这不是根本原因)
    2、管道文件中scrapy处理这些item对象也是异步的
        传递一次管道则会创建一个线程,然后按管道文件里的优先级进行数据的后期处理
"""

cmdline.execute('scrapy crawl maoyan'.split())