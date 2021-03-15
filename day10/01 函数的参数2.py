# 形参角度：
# 万能参数 1.*args,约定俗称：args  2.**kwargs
# 1.* 函数定义时，*代表聚合。他将所有位置参数聚合成一个元组，赋值给了args
# def eat(a, b, c, d):
#     print('吃：%s,%s,%s,%s'%(a, b, c, d))
#
# eat('haha', 'jj', 'ii', 'mm')
print()
# 需要一种参数可以接受所有实参 # 万能参数
# def eat(*args):
#     print(args)
#     print('吃：%s,%s,%s,%s'%args)
#
# eat('haha', 'jj', 'ii', 'mm')
# 练习客户端合法性：写一个函数：计算传入函数的所有参数的和
# def foo(*args):
#     count = 0
#     for i in args:
#         count += i
#     return count
# print(foo(1, 5, 6, 99, 8))

# **kwargs
# 函数的定义时：**将所有的关键字聚合到一个字典中，将这个字典赋值给kwargs
# def func(**kwargs):
#     print(kwargs)
#
# func(name='alex',age=73,sex='男')

# 形参角度的参数的顺序：位置参数，*args,默认参数，仅限关键字参数（了解）（这两个可互换），**kwargs
# def func(a, b, *args, sex='男', **kwargs):
#     print(a, b)
#     print(args)
#     print(sex)
#     print(kwargs)
#
#
# func(1, 2, 3, 4, 5, 6, sex='女', name='男', age=36)
# func(1, 2, 3, 4, 5, 6, name='男', age=36)

# 形式参数第四个参数：仅限关键字参数(在*args和**kwargs之间，必须以关键字参数对他进行传值)（了解）
# def func(a, b, *args, sex='男',c, **kwargs):
#     print(a, b)
#     print(args)
#     print(sex)
#     print(c)
#     print(kwargs)
#
#
# func(1, 2, 3, 4, 5, 6, sex='女', name='男', age=36, c='666')

# * 在函数调用时，*代表打散(元组)，**代表打散（字典）
def func(*args, **kwargs):
    print(args)
    print(kwargs)

# func([1, 2, 3], [22, 33])    #([1, 2, 3], [22, 33])
# func(*[1, 2, 3], *[22, 33])    #(1, 2, 3, 22, 33)
# func(*'sjdhiau', *'sks')    #('s', 'j', 'd', 'h', 'i', 'a', 'u', 's', 'k', 's')
func(**{'name':'哈哈'}, **{'age':19})    #func(name='哈哈',age=19)