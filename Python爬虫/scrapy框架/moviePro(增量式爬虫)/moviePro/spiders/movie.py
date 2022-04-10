import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from moviePro.items import MovieproItem

# 增量式爬虫：
# 概念:监测网站数据最新的情况，只爬取网站最新更新的数据
# 分析：
# --指定一个起始url
# --基于CrawlSpider获取其他页码链接
# --基于Rule将其他页码链接进行请求
# --从每一个页面对应的页面源码中解析出每一个电影详情页URL
# --检测电影详情页的url之前是否被请求过（存储到redis的set数据结构）
# --对详情页的url发起请求，然后解析出电影的名称和简介
# --进行持久化存储
 
class MovieSpider(CrawlSpider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.4567kp.com/frim/index1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/frim/index1-\d+\.html'), callback='parse_item', follow=True),
    )

    # 创建redis链接对象
    conn =Redis(host='127.0.0.1', port=6379)

    # 用于解析每一个页码对应页面中的电影详情页的url
    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            # 获取详情页的url
            detail_url = 'https://www.4567kp.com' + li.xpath('./div/a/@href').extract_first()
            # 将详情页的url存入redis的set中,创建一个urls集合并存入url：sadd urls www.xxx.com
            ex = self.conn.sadd('urls',detail_url)
            if ex == 1:
                print("该url没有被爬取过，可以进行数据爬取")
                yield scrapy.Request(url=detail_url,callback=self.parst_detail)
            else:
                print("数据还没有更新，暂无新数据可爬取")
    
    # 解析详情页中的电影名称和类型，进行持久化存储
    def parst_detail(self,response):
        item = MovieproItem()
        item['name'] = response.xpath('/html/body/div[1]/div/div/div/div[2]/h1/text()').extract_first()
        item['desc'] = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span/text()').extract()
        item['desc'] = ''.join(str(item['desc']))
        yield item

