import requests
from lxml import etree
# 利用代理服务器进行代理伪装爬虫访问(反制反爬机制封ip)
url = 'http://www.baidu.com/s?wd=ip'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
page_text = requests.get(url=url,headers=headers,proxies={"http":'http://3.211.17.212:80'}).text    
with open('./Demotmp/ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)



