# 默认参数的陷阱：
#
# def func(name, sex='男'):
#     print(name)
#     print(sex)
# func('alex')

# 陷阱只针对默认参数是可变的数据类型,那么你无论调用多少次这个默认参数。都是同一个
# 所以把默认参数是可变的数据类型想象成该数据类型保存在一个特殊的名称空间中
# Default values are computed once, then re-used.（官方文档）
# def func(name, alist=[]):
#     alist.append(name)
#     return alist
# ret1 = func('alex')
# print(ret1, id(ret1))
# ret2 = func('哈哈哈')
# print(ret2, id(ret2))

# 面试题1
# def func(a, list=[]):
#     list.append(a)
#     return list
# print(func(10, ))    # [10]
# print(func(20, []))  # [20]
# print(func(100, ))    # [10, 100]
# 面试题2
# def func(a, list=[]):
#     list.append(a)
#     return list
# ret1 = func(10, )
# ret2 = func(20, [])
# ret3 = func(100, )
# print(ret1)    # [10, 100]
# print(ret2)    # [20]
# print(ret3)    # [10, 100]



# 局部作用域的坑
# 1.
# count = 1
# def func():
#     count += 1
#     print(count)
# func()
# 2.
# 在函数中，如果你定义了一个变量，但是在定义这个变量之前对其引用了，那么解释器认为：语法问题
# 你应该在使用之前先定义
# count = 1
# def func():
#     print(count)    # UnboundLocalError: local variable 'count' referenced before assignment
#     count = 3
# func()
#

# global  nonlocal

# global
# 1.在局部作用域声明一个全局变量
# 2.修改一个全局变量
# name = 'alex'
# def func():
#     name = '哈哈哈'
#     print(name)
# func()
# print(name)

# name = 'alex'
# def func():
# #     global name
# #     name = '哈哈哈'
# #     print(name)
# # #
# # # print(name)    # alex
# # func()         # 哈哈哈
# # print(name)    # 哈哈哈
# # print(globals())

# 2.修改一个全局变量
# count = 1
# def func():
#     global count
#     count += 1
# print(count)
# func()
# print(count)

# nonlocal(用的少点)
# 1.不能操作全局变量
# count = 1
# def func():
#     nonlocal count
#     count += 1
# func()
# 2.局部作用域：内层函数对外层函数的局部变量进行修改
def wrapper():
    count = 1
    def inner():
        nonlocal count
        count += 1
    print(count)
    inner()
    print(count)
wrapper()