# 封闭的东西 ： 保证数据的安全

# 方案一：
# l1 = []    # 全局变量 数据不安全
# def make_averager(new_value):
#     l1.append(new_value)
#     total = sum(l1)
#     return total/len(l1)
# print(make_averager(10000))
# print(make_averager(11000))

# 方案二：数据安全，l1不能是全局变量
# l1 = []
# def make_averager(new_value):
#     l1 = []    # 函数调用后会结束
#     l1.append(new_value)
#     total = sum(l1)
#     return total/len(l1)
# print(make_averager(10000))
# print(make_averager(11000))

# 方案三：闭包
# def make_averager():
#     l1 = []    # 自由变量
#     def averager(new_value):
#         l1.append(new_value)
#         total = sum(l1)
#         return total/len(l1)
#     return averager
# avg = make_averager()    # avg = averager
# print(avg(100000))
# print(avg(110000))

# 闭包：多用于面试题  1.什么是闭包？2.闭包有什么作用？
# 1.什么是闭包？
# 1.闭包只能存在嵌套函数中
# 2.定义：内层函数对外层函数非全局变量的引用（使用），就会形成闭包
# 2.闭包有什么作用？
# 现象：被引用的非全局变量也称作自由变量，这个自由变量会与内层函数产生一个绑定关系，自由变量不会在内存中消失
# 闭包的作用：保证数据的安全

# 如何判断一个嵌套函数是不是闭包
# # 例一：是闭包
# def wrapper():
#     a = 1
#     def inner():
#         print(a)
#     return inner
# ret = wrapper()
# print(ret.__code__.co_freevars)
# # 例二：不是闭包
# a = 2
# def wrapper():
#     def inner():
#         print(a)
#     return inner
# ret = wrapper()
# ​
# ​
# # 例三：是闭包
# def wrapper(a,b):
#     def inner():
#         print(a)
#         print(b)
#     return inner
# a = 2
# b = 3
# ret = wrapper(a,b)

# 如何代码判断闭包？
# print(ret.__code__.co_freevars)


# 今日总结：
# 1.匿名函数
# 2.内置函数 ***
# 3.闭包