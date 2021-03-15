"""
无头浏览器的操作：无可视化界面的浏览器
    PhantomJs:停止更新了
    谷歌无头浏览器
让selenium规避检测
"""
# 使用的是谷歌无头浏览器
# from selenium import webdriver
# from time import sleep
#
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# # 后面是你的浏览器驱动位置，记得前面加'r'是防止字符转义的
# driver = webdriver.Chrome(r'chromedriver.exe', chrome_options=chrome_options)
# driver.get('https://www.cnblogs.com/')
# print(driver.page_source)
##########################################



#如何规避selenium被检测
# 查看是否被规避掉，在console中输入window.navigator.webdriver,返回undefined则爬虫有效，返回True则被网站规避掉
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(r'chromedriver.exe',options=option)
driver.get('https://www.taobao.com/')


















