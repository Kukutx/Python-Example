import requests
import re
import os
# 爬取糗事百科图片板块下的所有图片数据
if __name__=="__main__":
    # 创建文件夹用来保存所有图片，如果文件夹不存在就创建
    if not os.path.exists('./Demotmp/qiutuLibs'):               
        os.mkdir('./Demotmp/qiutuLibs')
    url="https://www.qiushibaike.com/imgrank/"        
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    # 使用通用爬虫对url对应网页进行爬取
    page_text = requests.get(url=url,headers=headers).text      
    # 使用聚焦爬虫讲页面所有的图片进行解析提取
    ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
    img_src_list = re.findall(ex,page_text,re.S)
    # print(img_src_list)
    for src in img_src_list:
        #拼接协议头
        src = 'https:' + src
        img_data = requests.get(url=src,headers=headers).content   
        # 生成图片名称
        img_name = src.split('/')[-1]
        # 图片存储路径
        imgPath = './Demotmp/qiutuLibs/' + img_name
        with open (imgPath,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功。')








