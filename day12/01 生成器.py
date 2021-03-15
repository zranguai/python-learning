# 生成器的本质就是迭代器
# 唯一的区别：生成器是我们用python代码构建的数据结构
# 迭代器都是提供的，或者转化得到的
# 获取迭代起的2种方法
# 1.3.python内部提供的
# 2.iter()方法
# 获取生成器的三种方式：
# 1.生成器函数
# 2.生成器表达式（自己写的）
# 3.python内部提供的一些

# 生成器函数(一个next()对应一个yield)
# def func():
#     print(111)
#     print(222)
#     yield 3
#     print('哈哈')
#     yield 4
# ret = func()
# print(next(ret))
# print(next(ret))
# print(next(ret))
# 一个next()对应一个yield

# return yield区别
# return: 函数中只存在一个return结束函数，并且给函数的执行者返回值
# yield: 只要函数中有yield那么他就是生成器函数而不是普通函数了
# 生成器函数可以存在多个yield(yield不会结束生成器函数)，一个yield对应一个next.

# 函数做的
# def func():
#     l1 = []
#     for i in range(1, 5001):
#         l1.append(f'{i}号包子')
#     return l1
# ret = func()
# print(ret)
# 迭代器做的
# def gen_func():
#     for i in range(1, 5001):
#         yield f'{i}号包子'
#
# ret = gen_func()
# # [1号包子] [2号包子] 每次只存在一个
# for i in range(200):
#     print(next(ret))
#
# for i in range(20):
#     print(next(ret))

# yield from(3.4版本更新)

# def func():
#     l1 = [1, 2, 3, 4, 5]
#     yield l1
# ret = func()
# print(next(ret))    # [1, 2, 3, 4, 5]

# yield from 将这个列表变成了迭代器返回
# def func():
#     l1 = [1, 2, 3, 4, 5]
#     yield from l1
""""
yield 1
yield 2
yield 3
yield 4
yield 5
"""
# ret = func()
# print(next(ret))    # 1
# print(next(ret))    # 2

# 练习题：小坑
def func():
    lst1 = ['卫龙', '老冰棍', '北冰洋', '牛羊配']
    lst2 = ['馒头', '花卷', '豆包', '大饼']
    yield from lst1
    yield from lst2


g = func()
print(g)
for i in range(8):
    print(next(g))
