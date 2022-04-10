import scrapy
from scrapy import item
from imgsPro.items import ImgsproItem

# 破解反爬机制 :图片懒加载
class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            # 因为反爬机制图片懒加载使用的是伪属性src2，也就是如果你是用浏览器的话，当你的页面出现在可视化区域的时候网页会将src2替换成src，
            # 但是由于我们使用的是爬虫所以不可能会有可视化区域所以只要写src2的伪属性就能获取解析了
            src =  'https:' + div.xpath('./div/a/img/@src2').extract_first()
            # print(src)
            item = ImgsproItem()
            item['src'] = src
            yield item
