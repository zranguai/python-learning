# 什么是装饰器
# 为什么不能改变原函数的调用方式
#     开放封闭原则
#     我们提前写好一个功能，让别人使用的时候能够直接使用就能完成相应的功能


# 登入
# 计算函数的执行时间

# 需求：
# 写了很多函数
# 添加日志： 在 时间 调用了什么函数
import time

def logger(path):
    def log(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            with open(path, mode='a', encoding='utf-8') as f:
                msg = f'{time.strftime("%Y-%m-%d %H:%M:%S")}执行了{func.__name__}'
                f.write(msg)
            return ret
        return inner
    return log
@logger('auth.log')
def login():
    print('登入的逻辑')

@logger('auth.log')
def register():
    print('注册的逻辑')

@logger('operate.log')
def show_goods():
    print('查看所有商品信息')

"""
@logger    # show_goods = logger(show_goods)
@logger('ashash')
    # log = logger('ashash')
    # @log --> show_goods = log(show_goods)
    # @logger('ashash')----------> show_goods = logger('ashash')(show_goods)
"""

@logger('operate.log')
def add_good():
    print('商品加入购物车')


# login()
# register()
# show_goods()
# add_good()
# 登入和注册的信息 写到auth.log文件里
# 所有的购物信息 写到operate.log文件里



# 总结：
def xxx(*args):    # 这里的参数是装饰器的参数
    def wrapper(f):    # 这里的f是被装饰的函数
        def inner(*args, **kwargs): # 这里的*args, **kwargs是被装饰函数的参数
            """"添加额外的功能：执行被装饰函数之前的操作"""
            ret = f(*args, **kwargs)
            """"添加额外的功能：执行被装饰函数之后的操作"""
            return ret  # 这里的ret是被装饰函数的返回值
        return inner    # 这里inner 等同于调用被装饰函数
    return wrapper
# 原本有一个装饰器wrapper
# @wrapper
# def func():
#   pass

# @xxx('参数')[这里的参数是装饰器的参数]   ===@wrapper
# def func():
#   pass


# 作业：带参数的装饰器作业
# 有100个函数，分别添加到一个计算函数执行时间的装饰器
# 有的时候需要计算时间，有的时候不需要
# 希望能通过修改一个变量，能控制这100个函数的装饰器是否执行
import time

def calc_time(flag):
    def wrapper(f):
        def inner(*args, **kwargs):
            if flag == True:
                start_time = time.time()
                ret = f(*args, **kwargs)
                end_time = time.time()
                chazhi = end_time - start_time
                print(f'该函数执行时间为{chazhi}')
            else:
                ret = f(*args, **kwargs)
                print('该函数不需要计算时间')
            return ret
        return inner
    return wrapper

@calc_time(True)
def foo1():
    time.sleep(1)
    print('函数1')

@calc_time(False)
def foo2():
    time.sleep(1)
    print('函数2')

def foo3():
    time.sleep(1)
    print('函数3')

def foo4():
    time.sleep(1)
    print('函数4')

def foo5():
    time.sleep(1)
    print('函数5')

def foo6():
    time.sleep(1)
    print('函数6')

foo1()
foo2()


















