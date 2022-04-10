from selenium import webdriver                           
from time  import sleep   
from selenium.webdriver.chrome.options import Options    
from selenium.webdriver import ChromeOptions    
# 实现无可视化
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 实现规避检测
option =ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
# 如何实现让selenium规避被检测风险
bro = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options,options=option)
# 无可视化界面（无头浏览器）
bro.get('https://www.baidu.com')
print(bro.page_source)
sleep(2)
bro.quit()