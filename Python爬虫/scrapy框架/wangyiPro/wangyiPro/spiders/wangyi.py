import scrapy
from scrapy import item
from selenium import webdriver
from wangyiPro.items import WangyiproItem

# 爬去网易新闻的新闻数据（标题和内容）
# 1.通过网易新闻的首页解析五大板块对应详情页的url
# 2.注意每一个板块的对应新闻标题都是动态加载的
# 3.通过解析出每一条新闻详情页的url获取详情页的页面源码解析出新闻内容
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    models_urls = []  # 存储五个板块对应的详情页url

    # 解析五大板块对应的详情页url
    # 实例化一个浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='./chromedriver')

    def parse(self, response):
        li_list = response.xpath(
            '//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [3, 4, 6, 7, 8]
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)
        # 依次对每一个板块对应的页面进行请求
        for url in self.models_urls:
            # 对每一个板块的url进行请求发送
            yield scrapy.Request(url, callback=self.parse_model)
    # 每一个板块对应的新闻标题相关的内容都是动态加载的

    def parse_model(self, response):
        # 解析每一个板块页面中对应新闻标题和新闻详情页的url
        div_list = response.xpath(
            '/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath(
                './div/div[1]/h3/a/@href').extract_first()
            item = WangyiproItem()
            item['title'] = title

            # 对新闻详情页的url发起请求
            yield scrapy.Request(url=new_detail_url, callback=self.parse_detail, meta={'item': item})
    # 解析新闻内容

    def parse_detail(self, response):
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content
        yield item
    # 关闭浏览器
    def closed(self,spider):
        self.bro.quit()
