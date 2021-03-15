"""
http://sc.chinaz.com/jianli/free.html 免费的简历模板进行爬取和保存
爬取前五页
"""
# import requests
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
# }
# from lxml import etree
# url = 'https://sc.chinaz.com/jianli/free.html'
# page_text = requests.get(url=url, headers=headers).text
# tree = etree.HTML(page_text)
# img_list = tree.xpath('//div[@id="container"]/div/a/img/@src')
# for img in img_list:
#     img = 'https:' + img
#     print(img)
# # print(img_list)


import requests
url = 'https://www.sogou.com/web'
wd = input('enter a key')
params = {
    'query': wd
}
response = requests.get(url=url, params=params)
response.encoding = 'utf-8'
page_text = response.text
filename = wd + '.html'
with open(filename, mode='w', encoding='utf-8') as fp:
    fp.write(page_text)