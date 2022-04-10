# import requests
# from lxml import etree
# from hashlib import md5
# # 模拟登录 + 打码平台 （失败）
# # 利用超级鹰进行验证码识别
# class Chaojiying_Client(object):
#     def __init__(self, username, password, soft_id):
#         self.username = username
#         password = password.encode('utf8')
#         self.password = md5(password).hexdigest()
#         self.soft_id = soft_id
#         self.base_params = {
#             'user': self.username,
#             'pass2': self.password,
#             'softid': self.soft_id,
#         }
#         self.headers = {
#             'Connection': 'Keep-Alive',
#             'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
#         }
#     def PostPic(self, im, codetype):
#         """
#         im: 图片字节
#         codetype: 题目类型 参考 http://www.chaojiying.com/price.html
#         """
#         params = {
#             'codetype': codetype,
#         }
#         params.update(self.base_params)
#         files = {'userfile': ('ccc.jpg', im)}
#         r = requests.post('http://upload.chaojiying.net/Upload/Processing.php',
#                           data=params, files=files, headers=self.headers)
#         return r.json()
#     def ReportError(self, im_id):
#         """
#         im_id:报错题目的图片ID
#         """
#         params = {
#             'id': im_id,
#         }
#         params.update(self.base_params)
#         r = requests.post(
#             'http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
#         return r.json()
# url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
# }
# page_text = requests.get(url=url, headers=headers).text
# tree = etree.HTML(page_text)
# code_img_src = 'https://so.gushiwen.cn' + \
#     tree.xpath('//*[@id="imgCode"]/@src')[0]
# code_img_data = requests.get(url=code_img_src, headers=headers).content
# with open('./Demotmp/codeimg.jpg', 'wb') as fp:
#     fp.write(code_img_data)
#     fp.close()
# # 进行识别
# chaojiying = Chaojiying_Client('kukutx', 'a65332120', '920277')
# im = open('./Demotmp/codeimg.jpg', 'rb').read()
# result = chaojiying.PostPic(im, 1902)
# # Post请求
# login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
# data = {
#     'from': 'http: // so.gushiwen.cn/user/collect.aspx',
#     'email': 'liuzhongli.ascii@gmail.com',
#     'pwd': 'a65332120',
#     'code': 'F3Z6',
#     'denglu': '登录'
# }
# # response = requests.post(url=login_url, headers=headers,data=data)
# # # 创建一个session对象
# session = requests.Session()
# response = session.post(url=login_url, headers=headers,data=data)
# # print(response.status_code)
# # login_page_text = requests.post(url=login_url, headers=headers,data=data).text
# # with open('./Demotmp/gushi.html','w',encoding='utf-8') as fp:
# #     fp.write(login_page_text)
# # 爬取当前用户对应的页面数据
# detail_url = 'https://so.gushiwen.cn/user/collect.aspx'

# detail_page_text = session.get(url=detail_url, headers=headers).text
# with open('./Demotmp/gushi.html','w',encoding='utf-8') as fp:
#     fp.write(detail_page_text)





# 利用Cookie进行爬取主页
import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
#登录后才能访问的网页
url = 'http://www.uzacg.live/home.php?mod=space&uid=179525'
#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'Hm_lvt_3258dba145510c95023172c72b4a63a3=1616510225,1616687328,1616869133,1617033904; _ga=GA1.2.1690344373.1617206090; _gid=GA1.2.559794503.1627516078; _gat_gtag_UA_178562510_1=1; DNmO_2132_noticeTitle=1; DNmO_2132_saltkey=BnxxhhIL; DNmO_2132_lastvisit=1627520662; DNmO_2132_sendmail=1; DNmO_2132_seccodecS=313.60dd3da1c323a14d2c; DNmO_2132_ulastactivity=1627524279%7C0; DNmO_2132_auth=a0152FcYfcmNKu0mYoRk8YqAgeMIwDGw4NV5VWaWZwQBeXqc2RNlPTzfS9GAmtrBTRenr8hZtaw6u%2BPnqHqJuZc9BjU; DNmO_2132_lastcheckfeed=179525%7C1627524279; DNmO_2132_checkfollow=1; DNmO_2132_lip=151.55.50.38%2C1627524279; DNmO_2132_sid=0; DNmO_2132_nofavfid=1; DNmO_2132_checkpm=1; DNmO_2132_home_diymode=1; DNmO_2132_lastact=1627524290%09home.php%09space'
#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
#设置请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}
#在发送get请求时带上请求头和cookies
resp = requests.get(url, headers = headers, cookies = cookies).text
with open('./Demotmp/Uzacg.html','w',encoding='utf-8') as fp:
    fp.write(resp)
