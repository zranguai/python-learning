# 整理今天笔记，课上代码最少敲3遍。
#
# 用列表推导式做下列小题
#
# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# l1 = ['ahsg', 'ahs', 'ajs', 'ss', 'asjhdua']
# l2 = [i.upper() for i in l1 if len(i) > 3]
# print(l2)
# 求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
# l1 = [(x, y) for x in range(0, 6, 2) for y in range(1, 6, 2)]
# print(l1)
# 求M中3,6,9组成的列表 M = [[1,2,3],[4,5,6],[7,8,9]]
# M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# l1 = [i[-1] for i in M]
# print(l1)
# 求出50以内能被3整除的数的平方，并放入到一个列表中。
# l1 = [i**2 for i in range(51) if i % 3 == 0]
# print(l1)
# 构建一个列表：['python1期', 'python2期', 'python3期', 'python4期',
# 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
# l1 = [f'python{i}期' for i in range(1, 11)]
# print(l1)
# 构建一个列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# l1 = [(i, i + 1) for i in range(6)]
# print(l1)
# 构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# l1 = [i for i in range(0, 19, 2)]
# print(l1)
# 有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']
# 将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']
# l1 = ['alex', 'WuSir', '老男孩', '太白']
# l1 = [l1[i] + f'{i}' for i in range(len(l1))]
# print(l1)
# 有以下数据类型：
#
x = {'name': 'alex',
     'Values': [{'timestamp': 1517991992.94, 'values': 100, },
                {'timestamp': 1517992000.94, 'values': 200, },
             {'timestamp': 1517992014.94, 'values': 300, },
            {'timestamp': 1517992744.94, 'values': 350},
            {'timestamp': 1517992800.94, 'values': 280}], }

# 将上面的数据通过列表推导式转换成下面的类型：
# [[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
# l1 = []
# for i in x['Values']:
#     l2 = []
#     l2.append(i['timestamp'])
#     l2.append(i['values'])
#     l1.append(l2)
# print(l1)
# l1 = [[i['timestamp'], i['values']] for i in x.get('Values')]
# print(l1)
# 用列表完成笛卡尔积
# 什么是笛卡尔积？ 笛卡尔积就是一个列表，
# 列表里面的元素是由输入的可迭代类型的元素对构成的元组，
# 因此笛卡尔积列表的长度等于输入变量的长度的乘积。
# [(),(),().....]
# ​	a. 构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色（列表里面的元素为元组类型)。
#
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# # [('S','black'),('S','white')]
# l1 = [(i, j) for i in sizes for j in colors]
# print(l1)
# ​	b. 构建一个列表,列表里面的元素是扑克牌除去大小王以后，所有的牌类（列表里面的元素为元组类型）。
#
# l1 = [('A','spades'),('A','diamonds'), ('A','clubs'), ('A','hearts')......('K','spades'),('K','diamonds'), ('K','clubs'), ('K','hearts') ]
# l1 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
# l2 = ['spades', 'diamonds', 'clubs', 'hearts']
# l3 = [(i, j) for i in l1 for j in l2]
# print(l3)
# print(len(l3))
#
# 简述一下yield 与yield from的区别。
#
# 看下面代码，能否对其简化？说说你简化后的优点？
#

# def chain(*args):
#     # ('abc',(0,1,2))
#     for it in args:
#         for i in it:
#             yield i
# g = chain('abc',(0,1,2))
# 简化
# def chain(*args):
#     yield from args
# g = chain(*'abc',*(0,1,2))
# for i in g:
#     print(i)
# 怎么让生成器产出值？
# next ，for 循环, 转化成list
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(list(g))
# print(list(g))  # 将迭代器转化成列表


# def chain(*args):
#     # ('abc',(0,1,2))
#     for it in args:
#         yield from it  # 'abc'  (0,1,2)
# g = chain('abc',(0,1,2))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# yield from 优化了内层循环，提高了效率。

# print(list(g))
# def func():
#     # yield [1,2,3]
#     yield from [1,2,3]
#     '''
#     yield 1
#     yield 2
#     yield 3
#     '''
# g = func()
# print(next(g))
# print(next(g))
# print(next(g))

# 看代码求结果（面试题）：
# v = [i % 2 for i in range(10)]
# print(v)    # [0,1,0,1,0,1,0,1,0,1]
# v = (i % 2 for i in range(10))
# print(v)    # (0, 1) 错误  <generator object <genexpr> at 0x00000191E9B9C248>
# print(next(v))
#
# for i in range(5):
#     print(i)    # 0,1,2,3,4
# print(i)    # 4
# 看代码求结果：（面试题）???(不懂)
# def demo():
#     for i in range(4):
#         yield i    # yield 0 yield 1 yield 2 yield 3
#
# g = demo()
# g1 = (i for i in g)
# g2 = (i for i in g1)
# print(list(g1))    # [0,1,2,3]
# print(list(g2))    # []  列表已经取完了
# 看代码求结果：（面试题）(不懂)
# def add(n, i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i    # yield 0 yield 1 yield 2 yield 3
#
# g = test()
# for n in [1, 10]:
#     g = (add(n, i) for i in g)
#
# print(list(g))    # [(1,0),(1,1),(1,2),(1,3),(2,0),(2,1)...]    # 错误
# 解释：
# 第一次循环：
# n = 1
# g = (add(n,i) for i in g)
# 第二次循环：
# n = 10
# g = (add(n,i) for i in g)
# list(g)--list((add(10, i) for i in (add(10, i) for i in test())))
# list(g)--list((add(10, i) for i in (add(10, i) for i in [0, 1, 2, 3])))
# list(g)--list((add(10, i) for i in ([10, 11, 12, 13]))
# [20, 21, 22, 23]
