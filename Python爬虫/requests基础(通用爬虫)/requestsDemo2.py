import requests
# 简易网页采集器
# UA伪装：              用于伪装爬虫程序为浏览器，误导服务器是浏览器发出请求（因为服务器会检测请求是否是浏览器发送的），（UA检测是反爬机制重要的一部分）
# UA: User-Agent       请求载体的身份标识
if __name__=="__main__":
    # UA伪装：将对应的User-Agent封装到字典里
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    # 指定url
    url="https://www.sogou.com/web"               #(注意?符号可保留也可不保留)
    # 处理url携带参数:封装到字典里(任何参数建议用字典封装保证可操控性)
    kw=input('enter a word:')
    param={
        'query':kw
    }
    # 发起请求,并带有参数并过程处理参数
    response = requests.get(url=url,params=param,headers=headers)                             
    # 获取响应数据
    page_text = response.text                    
    # 持久化存储
    with open('./requestsDemotmp/demo2.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
        fp.close()
    print('爬取数据结束')

