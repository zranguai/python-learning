"""
### 今日内容
- 数据解析
    - 数据解析的作用：
        - 可以帮助我们实现聚焦爬虫
    - 数据解析的实现方式：
        - 正则
        - bs4
        - xpath
        - pyquery
     - 数据解析的通用原理
         - 问题1:聚焦爬虫爬取的数据是存储在哪里的？
             - 都被存储在了相关的标签之中and相关标签的属性中
         - 1.定位标签
         - 2.取文本或者取属性333
"""
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
###################################
# 1.爬取byte类型数据(如何爬取图片)
# url = 'https://pic.qiushibaike.com/system/pictures/12223/122231866/medium/IZ3H2HQN8W52V135.jpg'
# img_data = requests.get(url=url).content
# with open('./img.jpg',mode='wb') as fp:
#     fp.write(img_data)
###################################
###################################
# 弊端：不能使用UA伪装
from urllib import request
# url = 'https://pic.qiushibaike.com/system/pictures/12223/122231866/medium/IZ3H2HQN8W52V135.jpg'
# request.urlretrieve(url, filename='./qutu.jpg')
#####################################

#####################################
import os
import re
# 糗图爬取1-3页所有的图片
# 1.使用通用爬虫将前3页对应的页面源码数据进行爬取
# 通用的url模板(不可变)
# 1.创建目录
# dirName = "./imgLibs"
# if not os.path.exists(dirName):
#     os.mkdir(dirName)
# url = f"https://www.qiushibaike.com/imgrank/page/%d/"
# # 2.下载图片
# for page in range(1, 3):
#     new_url = format(url%page)
#     page_text = requests.get(url=new_url,headers=headers).text    # 每一个页码对应的源码数据
#     ex = '<div class="thumb">.*?<img src="(.*?)".*?</div>'
#     img_src_list = re.findall(ex, page_text, re.S)
#     for src in img_src_list:
#         src = "https:" + src
#         img_name = src.split('/')[-1]
#         img_path = dirName + '/' + img_name    #./imgLibs/xxxx.jpg
#         request.urlretrieve(src, filename=img_path)
#         print(img_name, '下载成功')
##########################################
"""
- bs4解析
    - bs4解析的原理：
        - 实例化一个BeautifulSoup的对象，需要将即将被解析的页面源码数据加载到该对象中
        - 调用BeautifulSoup对象中的相关方法和属性进行标签定位和数据提取
    - 环境的安装：
        - pip install bs4
        - pip install lxml
    - BeautifulSoup的实例化：
        - BeautifulSoup(fp,'lxml'):将本地存储的一个html文档中的数据加载到实例化好的BeautifulSoup对象中
        - BeautifulSoup(page_text,'lxml'):将从互联网上获取的页面源码数据加载到实例化好的BeautifulSoup对象中
"""
"""
- 定位标签的操作：
    - soup.tagName：定位到第一个出现的tagName标签
    - 属性定位：soup.find('tagName',attrName='value')
    - 属性定位:soup.find_all('tagName',attrName='value'),返回值为列表
    - 选择器定位：soup.select('选择器'),返回的是列表
        - 层级选择器：>表示一个层级  空格表示多个层级
- 取文本
    - .string:获取直系的文本内容
    - .text:获取所有的文本内容
- 取属性
    - tagName['attrName']
"""
from bs4 import BeautifulSoup
fp = open('./test.html', mode='r', encoding='utf-8')
soup = BeautifulSoup(fp, 'lxml')
# 定位标签
# print(soup.div)    # 定位到第一个出现的div
# find相关
# print(soup.find('div', class_='song'))    # 只有class_标签需要带_
# print(soup.find('a', id='feng'))
# print(soup.find_all('div', class_='song'))    # 返回的是一个列表
# select相关
# print(soup.select('#feng'))    # 返回的是一个列表
# print(soup.select('.tang > ul >li'))    # 返回的是一个列表 > 表示一个层级
# print(soup.select('.tang li'))    # 返回一个列表  空格表示多个层级
# 取文本
# a_tag = soup.select("#feng")[0]
# print(a_tag.text)
# div = soup.div
# print(div.string)    # 取直系的文本内容
# div = soup.find('div', class_='song')
# print(div.string)
# a_tag = soup.select('#feng')[0]
# print(a_tag['href'])
#########################################################
# 爬取三国整篇内容（章节名称+章节内容）http://www.shicimingju.com/book/sanguoyanyi.html
# fp = open('./sanguo.txt', mode='w', encoding='utf-8')
# main_url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
# page_text = requests.get(url=main_url, headers=headers).text
# soup1 = BeautifulSoup(page_text, 'lxml')
# title_list = soup1.select('.book-mulu > ul > li > a')
# for page in title_list:
#     title = page.string
#     title_url = 'https://www.shicimingju.com' + page['href']
#     title_text = requests.get(url=title_url, headers=headers).text
#     # 解析详情页中的章节内容
#     soup = BeautifulSoup(title_text, 'lxml')
#     content = soup.find('div', class_='chapter_content').text
#     fp.write(title + ':' + content + '\n')
#     print(f'{title}下载成功')
############################################################
"""
- xpath解析
    - xpath解析的实现原理
        - 1.实例化一个etree的对象，然后将即将被解析的页面源码加载到改对象中
        - 2.使用etree对象中的xpath方法结合着不同形式的xpath表达式实现标签定位和数据提取
    - 环境安装：
        - pip install lxml
    - etree对象的实例化：
        - etree.parse('test.html')    # 本地文件
        - etree.HTML(page_text)    # 互联网页面
"""
"""
- xpath表达式:xpath方法的返回值一定是一个列表
    - 最左侧的/表示：xpath表达式一定要从根标签逐层进行标签查找和定位
    - 最左侧的//表示：xpath表达式可以从任意位置定位标签
    - 非最左侧的/:表示一个层级
    - 非最左侧的//：表示夸多个层级
    - 属性定位：//tagName[@attrName="value"]
    - 索引定位：//tagName[index] 索引是从1开始
- 取文本：
    - /text():直系文本内容
    - //text():所有的文本内容
- 取属性：
    - /@attrName
"""
################################################
from lxml import etree
# tree = etree.parse('./test.html')
# 标签定位
# print(tree.xpath('/html/head/title'))
# print(tree.xpath('//title'))
# print(tree.xpath('/html/body//p'))
# print(tree.xpath('//p'))
# 属性定位
# print(tree.xpath('//div[@class="song"]'))
# print(tree.xpath('//li[3]'))    # 返回的是一个对象地址
# 取文本
# print(tree.xpath('//a[@id="feng"]/text()')[0])    # 返回的是列表
# print(tree.xpath('//div[@class="song"]//text()'))    # 返回的是列表
# 取属性
# print(tree.xpath('//a[@id="feng"]/@href'))    # 返回的是列表
###############################################################
# 案例：爬取糗百中的段子内容和作者名称(未做完)
main_url = 'https://www.qiushibaike.com/text/'
page_text = requests.get(url=main_url, headers=headers).text
tree = etree.HTML(page_text)
div_list = tree.xpath('//div[@id="content"]//div[@class="col1 old-style-col1"]/div')
for div in div_list:
    author = div.xpath('//div[@class="author clearfix"]/a[2]//text()')[0]
    print(author)
# print(div_list)

###############################################################
# https://www.aqistudy.cn/historydata/ 爬取所有城市名称
# url = 'https://www.aqistudy.cn/historydata/'
# page_text = requests.get(url=url, headers=headers).text
# tree = etree.HTML(page_text)
# print(tree)
# city_list1 = tree.xpath('//div[@class="bottom"]/ul/li/a/text()')
# print(city_list1)
# city_list2 = tree.xpath('//ul[@class="unstyled"]//li/a/text()')
# print(city_list2)
# 利用|提高xpath的通用性(当前面表达式生效时执行前面，后面表达式生效时执行后面。两个同时生效时同时执行)
# cities = tree.xpath('//div[@class="bottom"]/ul/li/a/text() | //ul[@class="unstyled"]//li/a/text()')
# print(cities)



