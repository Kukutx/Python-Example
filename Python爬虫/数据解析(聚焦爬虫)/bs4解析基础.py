from bs4 import BeautifulSoup
# bs4 BeautifulSoup对象实例化
if __name__=="__main__":
    # 将本地的html文档中的数据加载到该对象
    fp = open('./Demotmp/test.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    # print(soup)
    # print(soup.a)   #soup.tagName 返回的是html文档元素中第一次出现的tagName标签
    # print(soup.div)   
    # print(soup.find('div'))     #获取标签等属性
    # print(soup.find('div',class_ = 'song'))     #属性定位 class_/id/attr
    # print(soup.find_all('a'))                   #获取所有符合要求的标签
    # print(soup.select('.tang'))                 #select选择器:可获取（id,class,标签等等），返回的是一个列表  
    # print(soup.select('.tang > ul > li >a')[0]) #层级选择器
    # print(soup.select('.tang > ul a')[0])   
    # print(soup.select('.tang > ul a')[0].text)  #获取标签之间的文本数据：string/text/get_text()  string:只获取该标签直系文本数据，text/get_text()：获取标签所有文本数据
    print(soup.select('.tang > ul a')[0].text['href']) 