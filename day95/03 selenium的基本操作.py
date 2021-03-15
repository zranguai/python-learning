from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get('https://www.jd.com/')
sleep(1)
# 进行标签定位
# 找到搜索框并输入
search_input = bro.find_element_by_id('key')
search_input.send_keys('mac pro')

# 点击搜索按钮
btn = bro.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
btn.click()
sleep(2)

# 执行js，进行滑动
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
page_text = bro.page_source
print(page_text)
sleep(2)
bro.quit()


