# Python urllib
# urllib 库用于操作网页 URL，并对网页的内容进行抓取处理。
# urllib 包含以下几个模块：
# urllib.request - 打开和读取 URL。
# urllib.error - 包含 urllib.request 抛出的异常。
# urllib.parse - 解析 URL。
# urllib.robotparser - 解析 robots.txt 文件。

# urllib.request
# request 定义了一些打开 URL 的函数和类，包含授权验证、重定向、浏览器 cookies等。可以模拟浏览器的一个请求发起过程。
# 可以使用 urllib.request 的 urlopen 方法来打开一个 URL，语法：urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, context=None)
# url：url 地址。
# data：发送到服务器的其他数据对象，默认为 None。
# timeout：设置访问超时时间。
# cafile 和 capath：cafile 为 CA 证书， capath 为 CA 证书的路径，使用 HTTPS 需要用到。
# context：ssl.SSLContext类型，用来指定 SSL 设置。
import urllib.request
import urllib.parse

# myURL = urllib.request.urlopen("https://www.runoob.com/")
# print(myURL.read())
# print(myURL.read(300))                    #read() 是读取整个网页内容，可以指定读取的长度
# print(myURL.readline())                   #读取一行内容
# lines = myURL.readlines()                 读取文件的全部内容
# for line in lines:
#     print(line)
# 简单的写入网页数据
# with open('./filetmp/urllib.html', 'wb') as f:
#     f.write(myURL.read())
#     f.close()  

# 获取状态码
# print(myURL.getcode())   
# try:
#     myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
# except urllib.error.HTTPError as e:
#     if e.code == 404:
#         print(404)   # 404

# URL 的编码与解码可以使用 urllib.request.quote() 与 urllib.request.unquote() 方法
# encode_url = urllib.request.quote("https://www.runoob.com/")  # 编码
# print(encode_url)
# unencode_url = urllib.request.unquote(encode_url)    # 解码
# print(unencode_url)

# 模拟头部信息
# 我们抓取网页一般需要对 headers（网页头信息）进行模拟
# 语法：urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# url：url 地址。
# data：发送到服务器的其他数据对象，默认为 None。
# headers：HTTP 请求的头部信息，字典格式。
# origin_req_host：请求的主机地址，IP 或域名。
# unverifiable：很少用整个参数，用于设置网页是否需要验证，默认是False。。
# method：请求方法， 如 GET、POST、DELETE、PUT等
# url = 'https://www.runoob.com/?s='  # 菜鸟教程搜索页面
# keyword = 'Python 教程'
# key_code = urllib.request.quote(keyword)  # 对请求进行编码
# url_all = url+key_code
# header = {
#     'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }   #头部信息
# request = urllib.request.Request(url_all,headers=header)
# reponse = urllib.request.urlopen(request).read()
# fh = open("./filetmp/urllib_test.html","wb")    # 将文件写入到当前目录中
# fh.write(reponse)
# fh.close()

# urllib.error
# urllib.error 模块为 urllib.request 所引发的异常定义了异常类，基础异常类是 URLError。
# urllib.error 包含了两个方法，URLError 和 HTTPError。
# URLError 是 OSError 的一个子类，用于处理程序在遇到问题时会引发此异常（或其派生的异常），包含的属性 reason 为引发异常的原因。
# HTTPError 是 URLError 的一个子类，用于处理特殊 HTTP 错误例如作为认证请求的时候，包含的属性 code 为 HTTP 的状态码，
# reason 为引发异常的原因，headers 为导致 HTTPError 的特定 HTTP 请求的 HTTP 响应头。
# 对不存在的网页抓取并处理异常
# import urllib.request
# import urllib.error
# myURL1 = urllib.request.urlopen("https://www.runoob.com/")
# print(myURL1.getcode())   # 200
# try:
#     myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
# except urllib.error.HTTPError as e:
#     if e.code == 404:
#         print(404)   # 404

# urllib.parse
# urllib.parse 用于解析 URL，语法：urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
# urlstring 为 字符串的 url 地址，scheme 为协议类型，
# allow_fragments 参数为 false，则无法识别片段标识符。相反，它们被解析为路径，参数或查询组件的一部分，并 fragment 在返回值中设置为空
o = urllib.parse.urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
print(o)
print(o.scheme)