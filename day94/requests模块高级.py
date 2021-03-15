# HttpConnectionPool:错误原因
#   原因：
#       1.短时间发起高频的请求导致ip被禁
#       2.http连接池中的连接资源被消耗尽
#   解决：
#       1.代理
#       2.headers中加入Conection: "close"
# ########################################
# 代理：代理服务器，可以接受请求然后将其转发
# 匿名度：
#   高匿：啥也不知道
#   匿名：知道你使用了代理，但是不知道你的真实ip
#   透明：知道你使用了代理并且知道你的真实ip
# 类型：
#   http
#   https
# 免费代理：
#   www.goubanjia.com
#   快代理
#   西祠代理xicidaili.com    # 网站目前挂掉了
#   http://http.zhiliandaili.cn/ :代理精灵(需要付费)
# cookie的处理
# ###########################################
# 使用代理的简单案例
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Connection': 'close'
}
# # url = 'https://www.baidu.com/s?wd=ip'
# url = 'http://ip.chinaz.com/'
# page_text = requests.get(url=url, headers=headers, proxies={'http': '123.169.122.111:9999'}).text
# with open('./ip.html', mode='w', encoding='utf-8') as fp:
#     fp.write(page_text)
############################################
# 代理池:构建自己的代理池
# import random
# proxy_list = {
#     {'https': '121.231.94.44:8888'},
#     {'https': '131.231.94.44:8888'},
#     {'https': '141.231.94.44:8888'}
# }
# url = 'https://www.baidu.com/s?wd=ip'
# page_text = requests.get(url=url, headers=headers, proxies=random.choice(proxy_list)).text
# with open('ip.html', 'w', enconding='utf-8') as fp:
#     fp.write(page_text)
# ##########################################
from lxml import etree
# # 从代理精灵中提取代理ip,为了获取一系列ip来构建自己的代理池
# ip_url = 'http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=1&fa=0&fetch_key=&groupid=0&qty=4&time=1&pro=&city=&port=1&format=html&ss=5&css=&dt=1&specialTxt=3&specialJson=&usertype=2'
# page_text = requests.get(ip_url, headers=headers).text
# tree = etree.HTML(page_text)
# ip_list = tree.xpath('//body//text()')
# print(ip_list)
# ####################################################
# 第一步:爬取ip,port http类型
# 爬取西祠代理(已挂)获取可用ip构建自己代理池
# import random
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
#     'Connection': "close"
# }
# # url = 'https://www.xicidaili.com/nn/%d'    # 西祠代理(已挂)
# url = 'https://www.kuaidaili.com/free/inha/%d/'
# proxy_list_http = []
# proxy_list_https = []
# for page in range(1, 20):
#     new_url = format(url%page)
#     ip_port = random.choice(ip_list)
#     page_text = requests.get(new_url, headers=headers, proxies={'https': ip_port}).text
#     tree = etree.HTML(page_text)
#     # tbody不可以出现在xpath表达式中
#     tr_list = tree.xpath('//*[@id="list"]/table//tr')[1:]    # 这里不能要tbody,索引是从1开始的
#     for tr in tr_list:
#         ip = tr.xpath('./td[1]/text()')[0]    # 返回的是一个列表
#         port = tr.xpath('./td[2]/text()')[0]
#         t_type = tr.xpath('/td[4]/text()')[0]
#         ips = ip+":" + port
#         if t_type == 'HTTP':
#             dic = {
#                 t_type: ips
#             }
#             proxy_list_http.append(dic)
#         else:
#             dic = {
#                 t_type: ips
#             }
#             proxy_list_https.append(dic)
# print(len(proxy_list_http), len(proxy_list_https))
#
# # 第二步: 检测,将可用的ip留下来
# for ip in proxy_list_http:
#     response = requests.get('https://www/sogou.com', headers=headers,proxies={'https': ip})
#     if response.status_code == '200':
#         print('检测到了可用的ip')
#########################################################
# cookie的处理:
#   手动处理:将cookie封装到headers中
#   自动处理: session对象.可以创建一个session对象,该对象可以像requests一样进行请求发送,不同之处在于如果在使用session进行
#            请求发送的过程中产生了cookie,则cookie会被自动存储在session对象中
#
# 案例:对雪球网中的新闻数据进行爬取https://xueqiu.com/
# 手动
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
#     'Cookie':'device_id=24700f9f1986800ab4fcc880530dd0ed; xq_a_token=db48cfe87b71562f38e03269b22f459d974aa8ae; xqat=db48cfe87b71562f38e03269b22f459d974aa8ae; xq_r_token=500b4e3d30d8b8237cdcf62998edbf723842f73a; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYwNjk2MzA1MCwiY3RtIjoxNjA1NTM1Mjc2NzYxLCJjaWQiOiJkOWQwbjRBWnVwIn0.PhEaPnWolUZRgyuOY-QO04Bn_A_HYU46Hm54_kWBxa8IZ6cFw20trOr7rKp7XztprxEFc7fkMN2_5abfh1TUyyFKqTDn7IfoThXyJ2lJCnH33q1q-K9BclYvLHrLGqt8jQ3YOJi7-nyiSb5ZTNk7TLEhiFfsbXaZK9evNrt7W65MdxoEWyCcGjbhI5znffRxDDLHD9511bd9upY9CUGbf4SHQwwx4PxyQqdy9j5bgqPN6rsuHoCvjcr42DZYRd8B72uQTkFs-Lnru4AFxt4o4gdaxPo_Qd_IqzCrXnwoLtCdX6n4NKV44SryBttE0SKQC6UbqC35PwN-JqPeWCHKpQ; u=201605535281005; Hm_lvt_1db88642e346389874251b5a1eded6e3=1605354060,1605411081,1605535282; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1605535282'
# }
# params = {
#     'status_id': '163425862',
#     'page': '1',
#     'size': '14'
# }
# url = 'https://xueqiu.com/statuses/reward/list_by_user.json?status_id=163425862&page=1&size=14'
# page_text = requests.get(url=url, headers=headers, params=params).json()
# print(page_text)
# 自动:将Cookie永久存储session
# 创建session对象
# session = requests.Session()
# session.get('https://xueqiu.com/', headers=headers)    # 自动处理cookie,将首页的cookie存储到session中，后面爬取其他页面时可以用到
# url = 'https://xueqiu.com/statuses/reward/list_by_user.json?status_id=163425862&page=1&size=14'
# page_text = session.get(url=url, headers=headers).json()
# print(page_text)
#############################################################
# 验证码的识别
#   超级鹰：http://www.chaojiying.com/about.html
#   注册：（用户中心身份）
#   登入：
#       创建一个软件：899370
#       下载实例代码
# 打码兔
# 云打码
# step1:超级鹰中的示例代码
import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):    # 用户名，密码，和软件id
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()
# step2:识别古诗文网中的验证码
def tranformImgData(imgPath, t_type):    # 验证码图片的地址和验证码的类型
    chaojiying = Chaojiying_Client('bobo328410948', 'bobo328410948', '899370')    # 需要注册的超级鹰的用户名，密码，和软件id
    im = open(imgPath, 'rb').read()
    return chaojiying.PostPic(im, t_type)['pic_str']    # t_type为该图片的类型码
# 从古诗文网中爬取验证码的图片，将图片保存到本地，然后将图片送入到超级鹰中识别，最后返回识别结果
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
page_text = requests.get(url, headers=headers).text
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.org'+tree.xpath('//*[@id="imgCode"]/@src')[0]    # 它返回的是一个列表
img_data = requests.get(img_src, headers=headers).content    # .content时爬取图片数据
with open('./code.jpg', 'wb') as fp:
    fp.write(img_data)
tranformImgData('./code.jpg', 1004)    # 将图片路径和图片类型输入进去，返回识别出来的码
##########################################################
# 重要 模拟登入，目的是为了将cookie保存到session中
# 将上述产生的验证码进行模拟登入
s = requests.Session()
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
page_text = s.get(url, headers=headers).text
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.org'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = s.get(img_src, headers=headers).content    # cookie的产生在发生验证码图片时产生,目的是：1.产生cookie，2：产生图片
with open('./code.jpg', 'wb') as fp:
    fp.write(img_data)

# 动态获取变化的参数
__VIEWSTATE = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
__VIEWSTATEGENERATOR = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]
# 获取前面超级鹰获得的验证码(将图片识别出来)
code_text = tranformImgData('./code.jpg', 1004)
print(code_text)    # 观察是否正确
# 该login_url是点击登入按钮后出现的页面，为post请求
login_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
data = {
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from':'http://so.gushiwen.org/user/collect.aspx',
    'email': 'www.zhangbowudi@qq.com',
    'pwd': 'bobo328410948',
    'code': code_text,
    'denglu': '登录',
}
page_text = s.post(url=login_url, headers=headers, data=data).text
with open('login.html', mode='w', encoding='utf-8') as fp:
    fp.write(page_text)
################################################################
# 动态变化的请求参数
#   通常情况下动态变化的请求参数都会被隐藏在前台页面页码中（也就是你登入的那个页面）
########################################################
from time import sleep
import time
from multiprocessing.dummy import Pool
start = time.time()
urls = {
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay'
}
def get_requests(url):
    page_text = requests.get(url).text
    print(page_text)
pool = Pool(3)
pool.map(get_requests, urls)    # 让自定义的函数去处理每一个线程函数
print('总耗时：', time.time()-start)
###########################################################
# 开启服务器
# from flask import Flask
# from time import sleep
# app = Flask(__name__)
# @app.route('/index')
# def index():
#     sleep(2)
#     return 'hello'
# @app.route('/index1')
# def index1():
#     sleep(2)
#     return 'hello1'
# if __name__ == '__main__':
#     app.run()
##########################################################
# ## 单线程+多任务异步协程
# - 协程
#     - 在函数（特殊的函数）定义的时候，如果使用了async修饰的话，则改函数调用后会返回一个协程对象，并且函数内部的实现语句不会被立即执行
# - 任务对象
#     - 任务对象就是对协程对象的进一步封装。任务对象==高级的协程对象==特殊的函数
#     - 任务对象时必须要注册到事件循环对象中
#     - 给任务对象绑定回调：爬虫的数据解析中
# - 事件循环
#     - 当做是一个容器，容器中必须存放任务对象。
#     - 当启动事件循环对象后，则事件循环对象会对其内部存储任务对象进行异步的执行。
# - aiohttp:支持异步网络请求的模块







