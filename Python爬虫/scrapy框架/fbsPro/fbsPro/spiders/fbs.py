import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fbsPro.items import FbsproItem
from scrapy_redis.spiders import RedisCrawlSpider     #分布式爬虫包


# 分布式爬虫：
# 概念：就是搭建一个分布式的机群，让其对一组资源进行分布联合爬取，其作用提升爬取效率
# 实现分布式:
# 安装scrapy-redis的组件，原生的scrapy是不能实现分布式爬虫的，必须和scrapy-redis结合使用，因为原生的scrapy调度器和管道是不能被分布式机群共享的所以不能实现分布式
# scrapy-redis可以给原生的scrapy框架提供被共享的管道和调度器

class FbsSpider(RedisCrawlSpider):                 #继承RedisCrawlSpider爬虫类
    name = 'fbs'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']

    # 添加新属性 sun 可以被共享调度器队列的名称
    redis_key = 'sun'

    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response)
        li_list = response.xpath('//div[2]/div[3]/ul[2]/li')
        for li in li_list:
            new_num = li.xpath('./span[1]/text()').extract_first()
            new_title = li.xpath('./span[3]/a/text()').extract_first()
            item =FbsproItem()
            item['title'] = new_title
            item['new_num'] = new_num
            yield item
