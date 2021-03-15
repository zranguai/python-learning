# 1.编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’。
# def wrapper(f):
#     def inner():
#         print('每次执行被装饰函数之前都得先经过这里')
#         r = f()
#         return r
#     return inner
# @wrapper    #func = wrapper(func)
# def func():
#     print('哈哈哈哈')
#
# func()
# 2.为函数写一个装饰器，把函数的返回值 +100 然后再返回。
# 装饰器：返回值加100
# def wrapper(f):
#     def inner(*args, **kwargs):
#         r = f(*args, **kwargs)
#         return r + 100
#     return inner
#
# @wrapper
# def handle(num1):
#     print(f'该数为{num1}')
#     return num1
#
# ret = handle(1)
# print(ret)
# 3.请实现一个装饰器，通过一次调用是函数重复执行5次。
# 装饰器，调用一次，函数执行5次
# def wrapper(f):
#     def inner():
#         count = 1
#         while count < 6:
#             f()
#             count += 1
#     return inner
#
# @wrapper
# def foo():
#     print('该函数要执行5次')
#
# foo()
# 4.请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中。
# import time
# def write_in(f):
#     def inner():
#         hand_time = time.time()
#         r = f()
#         print(r)
#         with open('haha', mode='w', encoding='utf-8') as f1:
#             f1.write(f'调用的函数名为{r},时间节点为{hand_time}')
#         return r
#     return inner
#
# @write_in
# def handle():
#     print('将该文件写入')
#     return 'handle'
#
# handle()


