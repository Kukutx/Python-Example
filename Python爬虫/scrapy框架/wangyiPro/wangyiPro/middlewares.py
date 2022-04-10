# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from time import sleep
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class WangyiproDownloaderMiddleware:

    def process_request(self, request, spider):
        return None
    # 该方法拦截五大板块对应的响应对象，进行篡改

    def process_response(self, request, response, spider):  # spider爬虫对象也就是爬虫文件里的对象
        bro = spider.bro            #获取了在爬虫类中定义的浏览器对象
        # 挑选出指定的响应对象进行篡改
        # 通过url指定request,然后指定response
        if request.url in spider.models_urls:
            bro.get(request.url)   #对五个板块对应的url进行请求
            sleep(3)
            page_text = bro.page_source             #包含了动态加载的新闻数据
            # response    #五大板块对应的响应对象
            # 针对定位到的这些response进行篡改
            # 实例化新的响应对象（符合需求：包含动态加载出的新闻数据），替代原来旧的响应对象
            # 基于selenium便捷的获取动态数据
            new_response = HtmlResponse(url = request.url, body = page_text, encoding = 'utf-8', request = request)
            return new_response
        else:
            return response    #其他请求对应的响应对象

    def process_exception(self, request, exception, spider):
        pass

  
