# 写函数，函数可以支持接收任意数字（位置传参）并将所有数据相加并返回。
# def sum1(*args):
#     count = 0
#     for i in args:
#         count += i
#     return count
#
#
# print(sum1(2, 5, 66, 9, 88, 7))
# 看代码写结果
#
#
# def func():
#     return 1, 2, 3
#
#
# val = func()
# print(type(val) == tuple)    #True
# print(type(val) == list)    #False
# 看代码写结果
#
#
def func(*args, **kwargs):
    print(args)
    print(kwargs)


# a. 请将执行函数，并实现让args的值为 (1,2,3,4)
# func(1, 2, 3, 4)
# b. 请将执行函数，并实现让args的值为 ([1,2,3,4],[11,22,33])
# func([1, 2, 3, 4], [11, 22, 33])
# c. 请将执行函数，并实现让args的值为 ([11,22],33) 且 kwargs的值为{'k1':'v1','k2':'v2'}
# func([11, 22], 33, k1='v1', k2='v2')
# d. 如执行 func(*{'武沛齐','金鑫','女神'})，请问 args和kwargs的值分别是？
# func(*{'武沛齐', '金鑫', '女神'})    # ('武沛齐', '金鑫', '女神')  {}
# e. 如执行 func({'武沛齐','金鑫','女神'},[11,22,33])，请问 args和kwargs的值分别是？
# func({'武沛齐', '金鑫', '女神'}, [11, 22, 33])    # ({'武沛齐', '金鑫', '女神'}, [11, 22, 33]) {}
# f. 如执行 func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})，请问 args和kwargs的值分别是？
# func('武沛齐', '金鑫', '女神', [11, 22, 33], **{'k1': '栈'})    # ('武沛齐', '金鑫', '女神', [11, 22, 33]) {'k1': '栈'}
# 看代码写结果
#
#
def func(name, age=19, email='123@qq.com'):
    print(name)
    print(age)
    print(email)
    pass

# # a. 执行 func('alex') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func('alex')    # 可以 name = 'alex',age=19,email='123@qq.com'
# # b. 执行 func('alex',20) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func('alex', 20)    # name = 'alex',age=20,email='123@qq.com'
# # c. 执行 func('alex',20,30) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func('alex', 20, 30)    # 可以 name = 'alex',age=20,email=30
# # d. 执行 func('alex',email='x@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func('alex',email='x@qq.com')    # 可以 name = 'alex',age=19,email='x@qq.com'
# # e. 执行 func('alex',email='x@qq.com',age=99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func('alex', email='x@qq.com', age=99)    # 可以 name = 'alex',age=99,email='x@qq.com'
# # f. 执行 func(name='alex',99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func(name='alex',99)    #不可执行
# # g. 执行 func(name='alex',99,'111@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func(name='alex',99,'111@qq.com')    #不可以
#
# 看代码写结果
#
#
# def func(users, name):
#     users.append(name)
#     return users
#
# result = func(['武沛齐', '李杰'], 'alex')
# print(result)    # ['武沛齐', '李杰', 'alex']
# 看代码写结果
#
#
# def func(v1):
#     return v1 * 2
#
#
# def bar(arg):
#     return "%s 是什么玩意？" % (arg,)
#
#
# val = func('你')    # '你你'
# data = bar(val)
# print(data)    # '你你'是什么玩意？
# 看代码写结果
#
#
# def func(v1):
#     return v1 * 2
#
#
# def bar(arg):
#     msg = "%s 是什么玩意？" % (arg,)
#     print(msg)  # '你你'是什么玩意？
#
#
# val = func('你')
# data = bar(val)
# print(data)  # None
# 看代码写结果
#
# v1 = '武沛齐'
#
#
# def func():
#     print(v1)    # '武沛齐' '老男人'
#
#
# func()
# v1 = '老男人'
# func()
# 看代码写结果
#

#
#
# v1 = '武沛齐'
# def func():
#     v1 = '景女神'
#     def inner():
#         print(v1)
#     v1 = '肖大侠'
#     inner()
#
# func()
# print(v1)
# v1 = '老男人'
# func()
# print(v1)
# '肖大侠'  '武沛齐'  '肖大侠'  '老男人'

# 看代码写结果【可选】
#
# def func():
#     data = 2 * 2
#     return data
#
#
# new_name = func
# val = new_name()
# print(val)    # 4
#
# # 注意：函数类似于变量，func代指一块代码的内存地址。
# 看代码写结果【可选】
#
# def func():
#     data = 2 * 2
#     return data
#
#
# data_list = [func, func, func]
# for item in data_list:
#     v = item()
#     print(v)    # 4 4 4
#
# # 注意：函数类似于变量，func代指一块代码的内存地址。
# 看代码写结果（函数可以做参数进行传递）【可选】

# def func(arg):
#     arg()
#
#
# def show():
#     print('show函数')


# func(show)    # 'show函数'
# 写函数，接收n个数字，求这些参数数字的和。（动态传参）
# def sum1(*args):
#     return sum(args)
#
# print(sum1(1, 2, 3, 4, 5))
# 读代码，回答：代码中, 打印出来的值a, b, c分别是什么？为什么？
#
# a = 10
# b = 20
# def test5(a, b):
#     print(a, b)    # 20 10
# c = test5(b, a)
# # c = test5(20, 10)
# print(c) # None

# 读代码，回答：代码中, 打印出来的值a, b, c分别是什么？为什么？
# a = 10
# b = 20
# def test5(a, b):
#     a = 20
#     b = 10
#     a = 3
#     b = 5
#     print(a, b)    # 3 5
# c = test5(b, a)
# # c = test5(20, 10)
# print(c)    # None
# 传入函数中多个列表和字典, 如何将每个列表的每个元素依次添加到函数的动态参数args里面？如何将每个字典的所有键值对依次添加到kwargs里面？
# 利用列表的打散*[] / 利用字典的打散 **{'k1': 'v1'}
# 写函数, 接收两个数字参数, 将较小的数字返回.
# def min1(a, b):
#     return a if a < b else b
# print(min1(100,30))
# 写函数, 接收一个参数(此参数类型必须是可迭代对象), 将可迭代对象的每个元素以’_’相连接, 形成新的字符串, 并返回.
# def chan(li):
#     s1 = '_'.join(li)
#     return s1
#
# chan(['1', '老男孩', '武sir'])
# 例如
# 传入的可迭代对象为[1, '老男孩', '武sir']
# 返回的结果为’1
# _老男孩_武sir’
#
# 19.
# 有如下函数:


# def wrapper():
#     def inner():
#         print(666)
#     inner()
#
# wrapper()
# 你可以任意添加代码, 执行inner函数.
#
# 相关面试题：
# 写出下列代码结果：
#
def foo(a, b, *args, c, sex=None, **kwargs):
    print(a, b)

    print(c)

    print(sex)

    print(args)

    print(kwargs)

# foo(1, 2, 3, 4, c=6)    # 1,2,6, None, (3,4) {}

# foo(1,2,sex='男',name='alex',hobby='old_woman')    # 错误

# foo(1,2,3,4,name='alex',sex='男')    # 错误

# foo(1,2,c=18)   #1，2，18，None（），{}

# foo(2, 3, [1, 2, 3],c=13,hobby='喝茶')    # 2,3 13, None,([1, 2, 3],){'hobby':'喝茶'}

# foo(*[1, 2, 3, 4],**{'name':'太白','c':12,'sex':'女'})    # 1,2,   12,   女      (3,4)  {'name':'太白’}
