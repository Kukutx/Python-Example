# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

# 下载中间件
class MiddleproDownloaderMiddleware:
    # UA池
    user_agent_list = [
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
           "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
           "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
           "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
           "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
           "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
           "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
           "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
           "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
           "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
           "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
           "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
           "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
           "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
           "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
           "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
           "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
           "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
           "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
           "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

    #可被选用的代理IP
    PROXY_http = [
        '153.180.102.104:80',
        '195.208.131.189:56055',
    ]
    PROXY_https = [
        '120.83.49.90:9000',
        '95.189.112.214:35508',
    ]
    # 拦截请求
    def process_request(self, request, spider):
        # UA伪装
        request.headers['User-Agent'] = random.choice(self.user_agent_list)


        # 为了验证代理的操作是否生效
        request.meta['proxy']='http://54.196.123.146:80'

        return None
    # 拦截所有响应
    def process_response(self, request, response, spider):
   
        return response
    # 拦截发生异常的请求
    def process_exception(self, request, exception, spider):
        if request.url.split(':')[0] == 'http':
            # 伪装代理（当请求出现异常了使用代理ip替换当前的ip可能是ip被禁了）
            request.meta['proxy']='http://' + random.choice(self.PROXY_http)
        else:
            request.meta['proxy']='https://' + random.choice(self.PROXY_https)
        return request     #将修正的请求对象进行的重新的请求发送
