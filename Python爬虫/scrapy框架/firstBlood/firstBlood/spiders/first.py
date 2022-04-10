import scrapy

class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称
    name = 'first'
    # 允许的域名:限定那些域名可以请求，start_urls
    # allowed_domains = ['www.baidu.com']
    # 起始url列表：该列表中存放的url会被自动进行请求发送
    start_urls = ['https://www.baidu.com/','https://www.sogou.com/']
    # 用作与数据解析:response表示请求的响应对象
    def parse(self, response):
        print(response)
