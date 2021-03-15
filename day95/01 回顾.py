"""
cookie的处理
    手动处理
        cookie从抓包工具中捕获封装到headers中
    自动处理
        session对象
代理
    代理服务器
        进行请求转发
        代理ip:port作用到proxies = {'http':'ip:port'}中
        代理池(列表)
验证码的识别
    超级鹰
模拟登入
    验证码的识别
    动态请求参数
    cookie
单线程+多任务异步协程
    协程
        如果一个函数的定义被asyic修饰后，则该函数调用后会返回一个协程对象。
    任务对象
        就是对协程对象的进一步封装
    绑定回调
        task.add_done_callback(func):func(task):task.result()
    事件循环对象
        事件循环对象是用来装载任务对象。该对象启动后，则会异步的处理调用其内部装载的每一个任务对象。(将任务对象手动进行挂起操作)
    aynic,await
--注意事项：在特殊函数内部不可以出现不支持异步模块的代码！！！否则将会中断整个异步的效果！！！
--aiohttp:支持异步请求的模块
"""
# 单线程+多任务异步协程
import aiohttp
import asyncio
import time
from lxml import etree
start = time.time()
urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]

# 特殊的函数：请求发送和响应数据的捕获
# 细节:在每一个with前加上async,在每一个阻塞操作的前边加上await
async def get_request(url):
    async with aiohttp.ClientSession() as s:    # 因为requests模块不能进行异步操作
        # s.get(url, headers=headers, proxy="http://ip:port", params)
        async with await s.get(url) as response:
            page_text = await response.text()    # read()返回的是byte类型的数据
            return page_text

# 回调函数(普通函数)：取其中需要的数据
def parse(task):
    page_text = task.result()
    tree = etree.HTML(page_text)
    parse_data = tree.xpath('//li/text()')
    print(parse_data)
# 多任务
tasks = []
for url in urls:
    c = get_request(url)
    task = asyncio.ensure_future(c)    # 封装一个任务对象
    task.add_done_callback(parse)    # 当任务对象执行完了之后才会回调
    tasks.append(task)

# 将多任务注册到事件循环当中
loop = asyncio.get_event_loop()    # 创建事件循环对象
loop.run_until_complete(asyncio.wait(tasks))    # 将任务对象注册到事件循环对象中，并开启事件循环对象,这里wait是挂起的意思

print(time.time()-start)











