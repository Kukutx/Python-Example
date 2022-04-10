from selenium import webdriver                           
from selenium.webdriver import ActionChains    
import time                       
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# 如果定位的标签存在于iframe标签之中则必须通过如下操作进行标签定位
bro.switch_to.frame('iframeResult')  #切换浏览器标签定位的作用域
div = bro.find_element_by_id('draggable')
# 动作链
action = ActionChains(bro)
# 点击长按指定的标签
action.click_and_hold(div)
for i in range(5):
    action.move_by_offset(17,0).perform()    #perform立即执行动作链操作
    time.sleep(0.3)
# 释放动作链
action.release()
bro.quit()