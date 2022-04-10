import requests
from hashlib import md5
from selenium import webdriver                           
from time  import sleep   
from PIL import Image
from selenium.webdriver import ActionChains  
# 利用超级鹰进行验证码识别
class Chaojiying_Client(object):
    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }
    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php',
                          data=params, files=files, headers=self.headers)
        return r.json()
    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post(
            'http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.maximize_window()                                         #最大化
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
sleep(1)
a_tag = bro.find_element_by_class_name('login-hd-account')
a_tag.click()
sleep(3)
bro.save_screenshot('./Demotmp/codepng.png')                       #进行当前全局的截图切保存
# 进行图片的裁剪
code_img_ele = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
location = code_img_ele.location
print('location:',location)
size = code_img_ele.size
print('size:',size)
rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))

i = Image.open('./Demotmp/codepng.png')
code_img_name = './Demotmp/code.png'
fram = i.crop(rangle)             #根据指定区进行图片裁剪
fram.save(code_img_name)

# 使用超级鹰进行识别
chaojiying = Chaojiying_Client('kukutx', 'a65332120', '920277')
im = open('./Demotmp/code.png', 'rb').read()
print(chaojiying.PostPic(im,9004)['pic_str'])
all_list = []                   #要存储即将被点击的点的坐标  [[x1,y1],[x2,y2]]
result = chaojiying.PostPic(im,9004)['pic_str']
if '|' in result:
    list_1 = result.split('|')
    print(list_1)
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(all_list)
#遍历列表，使用动作链对每一个列表元素对应的x,y指定的位置进行点击操作
for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()
    sleep(0.5)
#输入账号和密码
bro.find_element_by_id('J-userName').send_keys('xxxxxxx')
sleep(1)
bro.find_element_by_id('J-password').send_keys('xxxxxxx')
sleep(1)
bro.find_element_by_id('J-login').click()
sleep(3)
bro.quit()
