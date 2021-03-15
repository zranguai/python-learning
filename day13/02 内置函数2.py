# 重点学习
# 1.print()  # print(self, *args, sep=' ', end='\n', file=None)
# print(1, 2, 3, sep='|')
# print(1, end=' ')
# print(1, end=' ')
# 2.abs() *** 返回绝对值
# print(abs(-8))
# 3.sum() *** 求一个可迭代对象(int)的和(可以设置初始值)
# print(sum([1,2,3]))
# print(sum([1,2,3],10))
# 4.reversed() 将一个序列翻转, 返回翻转序列的迭代器
# l1 = [i for i in range(10)]
# l1.reverse()    # 列表的方法
# l2 = reversed(l1)  # 获取一个新的迭代器，对原列表没变化
# print(l1)
# print(list(l2))
# 5.zip() *** 拉链方法(经常出现在面试题)  函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组
# lst1 = [1,2,3]
# lst2 = ['a','b','c','d']
# lst3 = (11,12,13,14,15)
# obj = zip(lst1, lst2, lst3)    # python内部提供的迭代器
# print(obj)
# for i in obj:
#     print(i)
# print(list(obj))
# **********以下方法最重要*****
# 6.min()/max()
# l1 = [33, 2, 1, 55, 7, -1, -9]
# print(min(l1))
# 以绝对值的方式去获取最小值
# l2 = []
# func = lambda a: abs(a)
# for i in l1:
#     l2.append(func(i))
# print(min(l2))
# def abss(a):
#     return abs(a)
# print(min(l1, key=abss))
# 凡是可以加key的： 他会自动的将可迭代对象中的每个元素按照顺序传入key对应的函数中
# 以返回值比较大小

# 练习题1：求出值最小的键
# dic = {'a': 3, 'b': 2, 'c': 1}
# print(min(dic))    # 默认会按照字典的键比较大小
# def func(a):
#     return dic[a]    # 比较的是字典的值
# print(min(dic, key=func))  # 每次循环的是字典的键    # key=函数名
# print(min(dic, key=lambda a: dic[a]))

# 练习题2：
# l2 = [('哈1', 92), ('哈2', 73), ('哈3', 35), ('哈4', 41)]
# print(min(l2))
# print(min(l2, key=lambda args: args[1]))

# 7.sorted() 排序函数 可以加key
# sorted(l1, key=lambda x: x['sales_volumn'])
# l1 = [22, 33, 1, 2, 8, 7, 6, 5]
# l2 = sorted(l1)
# print(l1)
# print(l2)

# l2 = [('哈1', 92), ('哈2', 73), ('哈3', 35), ('哈4', 41)]
# print(sorted(l2, key=lambda x: x[1]))    # 返回的是一个列表  默认从低到高
# print(sorted(l2, key=lambda x: x[1], reverse=True))    # 返回的是一个列表  默认从低到高
# 8.filter() 类似与列表推导式的筛选模式
# l1 = [2, 3, 4, 1, 6, 7, 8]
# print([i for i in l1 if i > 3])    # 返回的是一个列表
# ret = filter(lambda x: x > 3, l1)  # 返回的是一个迭代器
# print(ret)    # ret是一个迭代器
# print(list(ret))

# 9.map() 类似与列表推导式的循环模式
# l1 = [1, 4, 6, 9, 16, 25]
# print([i**2 for i in range(1, 6)])    # 返回的是一个列表
# ret = map(lambda x: x**2, range(1, 6))    # 返回的是一个迭代器
# print(ret)
# print(list(ret))

# 10.reduce()
# from functools import reduce
# def func(x, y):
#     return x + y
# l = reduce(func, [1, 2, 3, 4])
# print(l)

