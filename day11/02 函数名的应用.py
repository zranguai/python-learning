# def func():
#     print(666)

# func()
# 1.函数名指向的是函数的内存地址
# 函数名 + （）就可以执行函数
# print(func, type(func))    # <function func at 0x000002924FE7C708> <class 'function'>
# 2.函数名就是变量
# f = func
# f1 = f
# func()
# f()
# f1()


# def func():
#     print('in func')
#
# def fun1():
#     print('in func1')
#
# func1 = func
# func1()

# 3.函数名可以作为容器类数据类型的元素

# def func1():
#     print(' in func1')
#
# def func2():
#     print(' in func2')
#
# def func3():
#     print(' in func3')
#
#
# l1 = [func1, func2, func3]
# for i in l1:
#     i()

# 4.函数名可以作为函数的参数
# def func():
#     print('in func')
#
# def func1(x):
#     x()
#     print('in func1')
#
# func1(func)

# 5.函数名可以作为函数的返回值
def func():
    print('in func')

def func1(x):
    print('in func1')
    return x

ret = func1(func)
ret()
