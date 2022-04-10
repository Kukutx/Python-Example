import requests
# 网络爬虫：通过编写程序，模拟浏览器上网然后将其去互联网上抓取数据
# 通用爬虫：就是尽可能的把互联网上的所有的网页下载下来，再对这些网页做相关处理(提取关键字、去掉广告)，或者获取接口的数据。
# 获取页面数据
if __name__=="__main__":
    # 指定url
    url="https://www.sogou.com/"
    # 发起请求
    response = requests.get(url=url)                #返回一个响应对象
    # 获取响应数据
    page_text = response.text                       #text返回的是字符串形式的响应数据
    # print(page_text)
    # 持久化存储
    with open('./requestsDemotmp/demo1.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
        fp.close()
    print('爬取数据结束')


    