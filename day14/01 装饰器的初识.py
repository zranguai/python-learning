# 装饰器（器：工具）
# 开放封闭原则：
# 开放：对代码的扩展是开放的
# 封闭：对源码的修改是封闭的

# 装饰器：完全遵循开放封闭原则
# 装饰器：在不改变原函数的代码以及调用方式的前提下，为其增加新的功能
# 装饰器就是一个函数，装饰器的本质就是闭包

# 版本1：大壮写一些代码测试一下index函数的执行效率
# 版本1重复代码过多
# import time
# def index():
#     time.sleep(2)    # 单位是秒
#     print('欢迎登入首页')
#
# def dariy():
#     time.sleep(2)    # 单位是秒
#     print('欢迎登入日记')
#
# # print(time.time())    # 格林威治时间
# start_time = time.time()
# index()
# end_time = time.time()
# print(end_time - start_time)
#
# start_time = time.time()
# dariy()
# end_time = time.time()
# print(end_time - start_time)
# 版本2：利用函数，解决代码重复使用问题
# 版本2还是有问题：虽然index函数的源码没变，给原函数添加了一个测试原函数效率的功能
# 但是原函数的调用方式发生改变了
# import time
# def index():
#     time.sleep(2)    # 单位是秒
#     print('欢迎登入首页')
#
# def dariy():
#     time.sleep(2)    # 单位是秒
#     print('欢迎登入日记')
#
# def timmer(f):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     print(end_time - start_time)
#
# timmer(index)

# 版本3：不能改变原函数的调用方式
# import time
# def index():
#     time.sleep(2)    # 单位是秒
#     print('欢迎登入首页')
#
# def dariy():
#     time.sleep(2)    # 单位是秒
#     print('欢迎登入日记')
#
# def timmer(f):    # f=index   (function index123)
#     def inner():
#         start_time = time.time()
#         f()    # index()
#         end_time = time.time()
#         print(end_time - start_time)
#     return inner    # function331144
# # timmer(index)  # ---> index()
# # ret = timmer(index)    # inner()
# # ret()    # inner()
# index = timmer(index)    # function331144
# index()    # inner()

# 版本4：python做了一个优化，提出了一个语法糖的概念（版本3有index = timmer(index) ）标准版的装饰器
# import time
# # timmer装饰器
# def timmer(f):    # f=index   (function index123)
#     def inner():
#         start_time = time.time()
#         f()    # index()
#         end_time = time.time()
#         print(end_time - start_time)
#     return inner    # function331144
#
# @timmer    #这句话等同于 index = timmer(index)    # function331144
# def index():
#     time.sleep(2)    # 单位是秒
#     print('欢迎登入首页')
#
# def dariy():
#     time.sleep(2)    # 单位是秒
#     print('欢迎登入日记')
#
# index()    # inner()
# dariy()

# 版本5：被装饰函数带返回值
# import time
# # timmer装饰器
# def timmer(f):    # f=index   (function index123)
#     # f = index
#     def inner():
#         start_time = time.time()
#         r = f()    # index()
#         end_time = time.time()
#         print(end_time - start_time)
#         return r
#     return inner    # function331144
#
# @timmer    #这句话等同于 index = timmer(index)    # function331144
# def index():
#     time.sleep(0.6)    # 单位是秒
#     print('欢迎登入首页')
#     return 666
# 加上装饰器不应该改变原函数的返回值，所以666应该返回给下面的ret,
# 但是下面的这个ret实际接受的是inner()函数的返回值，而666返回的是装饰器里面
# 的f(),也就是r,我们现在要解决的问题就是将r给inner的返回值
# ret = index()    # inner()
# print(ret)

# 版本6：被装饰函数带有参数
# import time
# # timmer装饰器
# def timmer(f):    # f=index   (function index123)
#     # f = index
#     def inner(*args, **kwargs):
#         # 函数的定义：* 聚合 args = ('零零', 18)
#         start_time = time.time()
#         r = f(*args, **kwargs)    # index()
#         # 函数的执行： * 打散：f(*args)--->f(*('零零', 18))--->f('零零', 18)
#         end_time = time.time()
#         print(end_time - start_time)
#         return r
#     return inner    # function331144
#
# @timmer    #这句话等同于 index = timmer(index)    # function331144
# def index(name):
#     time.sleep(0.6)    # 单位是秒
#     print(f'欢迎{name}登入首页')
#     return 666
# @timmer
# def dariy(name, age):
#     time.sleep(0.5)    # 单位是秒
#     print(f'欢迎{age}岁{name}登入日记')
# dariy('零零', 18)    # inner('零零', 18)
# index('哈哈')    # inner('哈哈')

# 标准版的装饰器
def wrapper(f):
    def inner(*args, **kwargs):
        """"添加额外的功能：执行被装饰函数之前的操作"""
        ret = f(*args, **kwargs)
        """"添加额外的功能：执行被装饰函数之后的操作"""
        return ret
    return inner
