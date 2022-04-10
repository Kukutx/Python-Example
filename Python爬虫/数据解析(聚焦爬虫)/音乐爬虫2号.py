from selenium import webdriver
import time
import re
import requests
import os
from selenium.webdriver import Chrome, ChromeOptions


def URL(a):
    driver.get('http://www.zgei.com/')
    driver.find_element_by_xpath('//*[@id="j-input"]').send_keys(a)
    driver.find_element_by_xpath('//*[@id="j-submit"]').click()
    time.sleep(2)
    url = driver.find_element_by_xpath('//*[@id="j-src-btn"]').get_attribute('href')
    return(url)

def DownloadFile(mp3_url,save_url,file_name):
    try:
        if mp3_url is None or save_url is None or file_name is None:
            print('参数错误')
            return None
        # 文件夹不存在，则创建文件夹
        folder = os.path.exists(save_url)
        if not folder:
            os.makedirs(save_url)
        # 读取MP3资源
        res = requests.get(mp3_url,stream=True)
        # 获取文件地址
        file_path = os.path.join(save_url, file_name)
        print('开始写入文件：', file_path)
        # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
        with open(file_path, 'wb') as fd:
            for chunk in res.iter_content():
                fd.write(chunk)
        print(file_name+' 成功下载！')
    except:
        print("程序错误")
if __name__ == "__main__":
    opt = ChromeOptions()            # 创建Chrome参数对象
    opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
    driver = Chrome(options=opt)     # 创建Chrome无界面对象
    a = input('请输入你想下载的歌名：')
    driver = Chrome(options=opt)
    file_name = str(a)+'.mp3'
    save_url='C:/Users/liuzh/Downloads/test/爬虫数据/'
    url = URL(a)
    DownloadFile(url,save_url, file_name)
    driver.close()