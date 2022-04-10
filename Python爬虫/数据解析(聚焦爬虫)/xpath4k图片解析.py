import requests  
import os
from lxml import etree   
#爬起4k图片解析                   
if __name__ == "__main__":
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    url = 'https://pic.netbian.com/4kmeinv/'
    response = requests.get(url=url,headers=headers)
    # response.encoding = 'utf-8'                           #可以手动设定响应数据的编码格式
    # response.encoding = response.apparent_encoding
    page_text = response.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    if not os.path.exists('./Demotmp/picLibs'):
        os.mkdir('./Demotmp/picLibs')
    for li in li_list:
        img_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')             #转编码
        # print(img_name,img_src)
        # 请求图片进行持久化存储
        img_data = requests.get(url=img_src,headers=headers).content
        img_path = './Demotmp/picLibs/' + img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print('下载成功')

   
