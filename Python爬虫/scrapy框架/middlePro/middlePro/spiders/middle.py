import scrapy

# 中间件可以实现：
# 拦截请求：
#     -可修改UA伪装（我们是可以是可以直接使用UA最为请求头但是那种是全局的也就是所有请求统一使用那个UA，而中间件可以拦截每一个请求对象而我们可以修改不同的载体标识）
#     -代理IP
# 拦截响应：
#     -篡改响应数据
#     -响应对象
 
class MiddleSpider(scrapy.Spider):
    # 爬取百度
    name = 'middle'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response):
        page_text = response.text
        with open('./ip.html','w',encoding='utf-8') as fp:
            fp.write(page_text)

