import requests
import os
from lxml import etree
# 批量下载简历模板
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    param = input("请输入页数：")
    if not param:
       url = 'https://sc.chinaz.com/jianli/free.html'
    elif param == str(1):
        url = 'https://sc.chinaz.com/jianli/free.html'
    else:
        param = '_' + param
        url = 'https://sc.chinaz.com/jianli/free{}.html'.format(param)
    response = requests.get(url=url,headers=headers)
    response.encoding = response.apparent_encoding
    page_text = response.text
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="main_list jl_main"]/div')
    if not os.path.exists('./Demotmp/Mobang'):
      os.mkdir('./Demotmp/Mobang')
    for div in div_list:
        url_src ='https:' + div.xpath('./p/a/@href')[0]
        url_response = requests.get(url=url_src,headers=headers)
        url_response.encoding = url_response.apparent_encoding
        url_page_text = url_response.text
        url_tree = etree.HTML(url_page_text)
        url_name = url_tree.xpath('//div/h1/text()')[0]
        get_zip = url_tree.xpath('//ul[@class="clearfix"]/li[1]/a/@href')[0]
        get_data = requests.get(url=get_zip,headers=headers).content
        url_path = './Demotmp/Mobang/' + url_name + '.zip'
        with open(url_path,'wb') as fp:
            fp.write(get_data)
            print('下载成功')

















