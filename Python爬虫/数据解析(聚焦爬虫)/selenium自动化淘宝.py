from selenium import webdriver                           #基于浏览器的自动化模块                     
import time      

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://world.taobao.com/')
# 标签定位
search_input = bro.find_element_by_class_name('rax-textinput')
# 标签交互
search_input.send_keys('Iphone')
# 执行一组js程序
bro.execute_script('window.scroll(0,document.body.scrollHeight)')
time.sleep(2)
# 点击搜索按钮
btn = bro.find_element_by_css_selector('.search-button')
btn.click()
bro.get("https://www.baidu.com")
time.sleep(2)
# 回退
bro.back()
time.sleep(2)
# 前进
bro.forward()
time.sleep(5)
bro.quit()

