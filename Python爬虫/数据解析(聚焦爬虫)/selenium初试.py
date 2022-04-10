from selenium import webdriver                           #基于浏览器的自动化模块
from lxml import etree                        
import time                        
# 实例化浏览器对象（传入浏览器驱动程序路径）
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# 让浏览器发期一个url请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
# 获取浏览器当前页面源码数据
page_text = bro.page_source

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
time.sleep(5)
bro.quit()        #关闭浏览器



