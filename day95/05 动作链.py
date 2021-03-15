"""
动作链：
    一系列连续的动作
    在实现标签定位时，如果发现定位的标签是存在于iframe标签之中的，则在定位时必须执行一个
    固定的操作：bro.switch_to.frame('id')
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-example-draggable')
# 如果里面还嵌套了iframe
bro.switch_to.frame('iframeResult')

div_tag = bro.find_element_by_id('draggable')
print(div_tag)

# 拖动=点击+滑动
action = ActionChains(bro)
action.click_and_hold(div_tag)

for i in range(5):
    # perform让动作链立即执行
    action.move_by_offset(17, 0).perform()
    sleep(0.5)
action.release()    # 让action回收一下

sleep(3)
bro.quit()









