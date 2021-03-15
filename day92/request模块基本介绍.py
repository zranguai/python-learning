"""
- 什么是requests模块？
    - Python中封装好的一个基于网络请求的模块。
- requests模块的作用？
    - 用来模拟浏览器发请求
- requests模块的环境安装：
    - pip install requests
"""
"""
requests模块的编码流程
    1.指定url
    2.发起请求
    3.获取响应数据
    4.持久化存储
"""
##########################
# # 爬取搜狗首页源码数据
# import requests
# # 1.指定url
# url = 'https://www.sogou.com/'
# # 2.请求发送get:get返回值是一个响应对象
# response = requests.get(url=url)
# # 3.获取响应数据
# page_text = response.text    # 返回的是字符串形式的响应数据
# # 4.持久化存储
# with open('sogou.html',mode='w',encoding='utf-8') as fp:
#     fp.write(page_text)
#############################
#############################
# 实现一个简易的网页采集器
# 需要让url携带的参数动态化
# import requests
# url = 'https://www.sogou.com/web'
# # 实现参数动态化
# wd = input('enter a key:')
# params = {
#     'query': wd
# }
# # 在请求中需要将请求参数对应的字典作用到params这个get方法的参数中
# response = requests.get(url=url, params=params)
#
# page_text = response.text
# file_name = wd+'.html'
# with open(file_name,encoding='utf-8',mode='w') as fp:
#     fp.write(page_text)
################################
"""
上述代码运行后发现：
    1.出现了乱码
    2.数据量级不对
"""
##################################
# 解决乱码：解决响应数据的编码方式
# import requests
# url = 'https://www.sogou.com/web'
# wd = input('enter a key')
# params = {
#     'query': wd
# }
# response = requests.get(url=url, params=params)
# response.encoding = 'utf-8'
# page_text = response.text
# filename = wd + '.html'
# with open(filename, mode='w', encoding='utf-8') as fp:
#     fp.write(page_text)
####################################
"""
UA检测：门户网站通过检测请求载体的身份标识判定该请求是否为爬虫发起的请求
UA伪装：Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36
"""
###################################
# import requests
# url = 'https://www.sogou.com/web'
# wd = input('enter a key')
# params = {
#     'query': wd
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
# }
# response = requests.get(url=url, params=params, headers=headers)
# response.encoding = 'utf-8'
# page_text = response.text
# filename = wd + '.html'
# with open(filename, mode='w', encoding='utf-8') as fp:
#     fp.write(page_text)
######################################
"""
#爬取的是豆瓣电影中电影的详情数据https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action=
#分析：当滚动条被滑动到页面底部的时候，当前页面发生了局部刷新（ajax的请求）

动态加载的页面数据
是通过例一个单独的请求请求到的数据
"""
######################################
# import requests
# url = 'https://movie.douban.com/j/chart/top_list'
# start = input('电影开始')
# end = input('电影结束')
# dic = {
#     'type': '13',
#     'interval_id': '100:90',
#     'action': '',
#      'start': start,
#      'end': end
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
# }
# response = requests.get(url=url, params=dic, headers=headers)
# page_text = response.json()    # json返回的是序列化好的实例对象
# for dic in page_text:
#     print(dic['title']+dic['score'])
##########################################

#########################################
# 肯德基餐厅查询http://www.kfc.com.cn/kfccda/storelist/index.aspx
# 注意：get请求参数时params,但是post请求参数时data
# import requests
# url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
# site = input('请输入地点>>')
# for page in range(1, 5):
#     data = {
#         'cname':'',
#             'pid':'',
#     'keyword': site,
#     'pageIndex': '1',
#     'pageSize': '10'
#     }
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
#     }
#     response = requests.post(url=url, data=data,headers=headers)
#     print(response.json())

###################################################################
# 作业
# 需求：
"""
- 如何检测页面中是否存在动态加载的数据？
    - 基于抓包工具实现
        - 先捕获网站请求后所有的数据包
        - 在数据包中定位到地址栏所对应请求的数据包，在response选项卡对应的数据中进行局部搜索（页面中的某一组内容）
            - 可以搜索到：爬取的数据不是动态加载的
            - 没有搜索到：爬取的数据是动态加载的
        - 如何定位动态加载的数据在哪个数据包中呢？
            - 进行全局搜索
+ 其中一家企业详情页：（id不同）http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=ff83aff95c5541cdab5ca6e847514f88
+ 例外一家企业详情页        http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=266cff22d9d24ba98d16acf379c1f58d
"""
import requests
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

data = {
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn':''
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
response = requests.post(url=url, data=data, headers=headers)
# ###################
temp = []
for i in range(5):
    ret = response.json()['list'][i]['ID']
    temp.append(ret)
print(temp)
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for i in range(5):
    print(temp[i])
    ret1 = temp[i]
    data = {
        'id': ret1
    }
    response = requests.post(url=url, data=data, headers=headers)
    print(response.json())

"""
http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=ff83aff95c5541cdab5ca6e847514f88
其中一个详情页(带企业负责人名字)http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
例外一个详情页(带企业负责人名字)http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
id: ff83aff95c5541cdab5ca6e847514f88
"""

