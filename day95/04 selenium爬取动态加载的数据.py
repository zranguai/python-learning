from selenium import webdriver
from time import sleep
from lxml import etree
bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('http://scxk.nmpa.gov.cn:81/xk/')
sleep(2)
page_text = bro.page_source
page_text_list = [page_text]

for i in range(3):
    bro.find_element_by_id('pageIto_next').click()    # 点击下一页
    sleep(2)
    page_text_list.append(bro.page_source)

for page_text in page_text_list:
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@id="gzlist"]/li')
    for li in li_list:
        title = li.xpath('./dl/@title')[0]
        num = li.xpath('./ol/@title')[0]
        print(title, num)

sleep(2)
bro.quit()














