import requests  
from lxml import etree   
#爬起58二手房中房源信息                   
if __name__ == "__main__":
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    url = 'https://www.58.com/ppkchuzu671'
    page_text = requests.get(url=url,headers=headers).text
    # 数据解析
    tree = etree.HTML(page_text)
    fp = open('./Demotmp/demo2.txt','w',encoding='utf-8')
    li_list = tree.xpath('//ul[@class="list"]/li')
    for li in li_list:
        title = li.xpath('./a/div[2]/p[1]/text()')[0]
        fp.write(title + '\n')
        print(title,"爬取成功。")

   
