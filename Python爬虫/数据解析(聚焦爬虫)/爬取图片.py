import requests
# 爬取图片
if __name__=="__main__":
    url="https://www.runoob.com/wp-content/uploads/2013/12/java.jpg"    
    img_data = requests.get(url=url).content                      #返回二进制对象       
    with open('./Demotmp/demo1.jpg','wb') as fp:
        fp.write(img_data)
        fp.close()
    print('爬取数据结束')

