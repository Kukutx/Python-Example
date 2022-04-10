import scrapy
from qiubaiPro.items import QiubaiproItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     # 解析：作者的名称+段子内容
    #     div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data = []       #存储所有解析到的数据
    #     for div in div_list:
    #         # xpath返回的是列表，但是列表元素一定是Selector类型对象
    #         # extract可以将Selector对象中的data参数存储的字符串提取出来
    #         author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         # print(author,content)
    #         # break
    #         dic={
    #             'authonr':author,
    #             'content':content,
    #         }
    #         all_data.append(dic)
    #     return all_data

    #基于管道永久化存储  
    def parse(self, response):
       # 解析：作者的名称+段子内容
       div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
       all_data = []       #存储所有解析到的数据
       for div in div_list:
           # xpath返回的是列表，但是列表元素一定是Selector类型对象
           # extract可以将Selector对象中的data参数存储的字符串提取出来
        #    author = div.xpath("./div[1]/a[2]/h2/text()")[0].extract()
           author = div.xpath("./div[1]/a[2]/h2/text() | ./div[1]/span/h2/text()")[0].extract()
           content = div.xpath("./a[1]/div/span//text()").extract()
           content = ''.join(content)
           item = QiubaiproItem()
           item['author'] = author
           item['content'] = content
           yield item    #将item提交给了管道


          
