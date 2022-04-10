import requests  
import os
from lxml import etree   
#爬起所有城市名称                  
if __name__ == "__main__":
    # 用法一
    # headers={
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    # }
    # url = 'https://www.aqistudy.cn/historydata/'
    # page_text = requests.get(url=url,headers=headers).text
    # tree = etree.HTML(page_text)
    # host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names = []
    # #解析所有热门城市的名称
    # for li in host_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(hot_city_name)
    # city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # # 解析全部城市的名称
    # for li in city_names_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    # print(all_city_names,len(all_city_names))
    

    #用法二 
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a  |  //div[@class="bottom"]/ul/div[2]/li/a')     #|：或者
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names,len(all_city_names))
   
