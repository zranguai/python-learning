# recursion递归
# 递归的最大深度1000层（官网规定）:节省内存空间
# 1.递归要尽量控制次数
# 2.循环和递归的关系
#     递归不是万能的
#     递归比起循环来说更占内存
#
# 可以修改递归的最大深度
# import sys
# sys.setrecursionlimit(2000)

# count = 0
# def func():
#     global count
#     count += 1
#     print(count)
#     func()
#
# func()


# 结束递归
# count = 0
# def func():
#     global count
#     count += 1
#     print(count)
#     if count == 3:
#         return
#     func()
#     print(456)
#
# func()

# 函数的调用
# 函数的参数
# 函数的返回值

# 一个递归函数想要结束，必须再函数内写一个return，并且return的条件必须是一个可以达到的条件
# 并不是函数中有return，return的结果就一定能够再调用函数的外层接受到
# def func1(count):
#     count += 1
#     print(count)
#     if count == 5:
#         return 5
#     ret = func1(count)
#     return ret    # 上面两段等同于 return func1(count)(先执行再return)
#     # print(count, ret)
#     # return ret
#
# print('-->', func1(1))



# 先写正则相关的题
# 递归相关

# 练习题：
# 1.计算阶乘  100！
# def foo(n):
#     if n == 1:
#         return 1
#     return n * foo(n - 1)
# ret = foo(5)
# print(ret)
    # 循环
    # 递归
# 2.os模块：查看一个文件夹下的所有文件，这个文件夹下面还有文件，不能用walk
# import os
# def look_(path, allfile):
#     filelist = os.listdir(path)
#     for i in filelist:
#         filepath = os.path.join(path, i)
#         if os.path.isdir(filepath):
#             look_(filepath, allfile)
#         else:
#             allfile.append(filepath)
#     return allfile

# 9月5号下午作业:
# haha--->测测1
# haha--->测测2
import os
def look_(path):
    filelist = os.listdir(path)
    for i in filelist:
        filepath = os.path.join(path, i)
        if os.path.isfile(filepath):
            print(i)
        elif os.path.isdir(filepath):
            look_(filepath)
# ret = look_('D:\老男孩python22期代码及笔记\day20')
# print(ret)

# 9月5号下午继续搞这个
# 3.os模块：查看一个文件夹下所有文件的大小，这个文件夹下面还有文件，不能用walk
# 方法1
# import os
# def get_FileSize(filePath):
#     fsize = os.path.getsize(filePath)
#     fsize = fsize/1024
#     return f'{round(fsize, 2)}KB'
#
# def look_(path, allfile):
#     filelist = os.listdir(path)
#     for i in filelist:
#         filepath = os.path.join(path, i)
#         rfp = filepath
#         if os.path.isdir(filepath):
#             look_(filepath, allfile)
#         else:
#             allfile.append(filepath + f'文件大小为{get_FileSize(rfp)}')
#     return allfile

# ret = look_('D:\老男孩python22期代码及笔记', [])
# print(ret)
# 方法2：
def dur_size(path):
    filelist = os.listdir(path)
    size = 0
    for name in filelist:
        filepath = os.path.join(path, name)
        if os.path.isfile(filepath):
            size += os.path.getsize(filepath)
        else:
            ret = dur_size(filepath)
            size += ret
        print(filepath)
    return size

# ret = dur_size('D:\老男孩python22期代码及笔记\day20')
# print(ret)
# 4.计算斐波那契数列 （找第一百个数） # 1 1 2 3 5 8 13 21 34 55
# a:递归做 (速度极慢)
# def foo1(n):
#     if n == 1 or n == 2:
#         return 1
#     return foo1(n - 1) + foo1(n - 2)
# ret = foo1(10)
# print(ret)
# b.递归加强版（速度较块）
# def fib(n, a=1, b=1):
#     if n == 1 or n == 2:
#         return b
#     else:
#         a, b = b, a + b
#         return fib(n-1, a, b)
# ret = fib(100)
# print(ret)
# c:循环做(速度快)
# def fib(n):
#     a = 1
#     b = 1
#     while n > 2:
#         a, b = b, a + b
#         n -= 1
#     return b

# 用生成器来写
def fib(n):
    a = 1
    if n == 1:
        yield
        return
    yield a
    b = 1
    yield b
    while n > 2:
        a, b = b, a + b
        yield b
        n -= 1

# for i in fib(10):
#     print(i)
# ret = fib(100)
# print(ret)
# 5.三级菜单  可能n级

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
def tree_menu(menu):
    flag = True
    while flag:
        for i in menu.keys():
            print(i)
        key = input('输入>>>')
        if key == 'b':
            return True
        elif key == 'q':
            return False
        elif menu.get(key):
            dic = menu[key]
            ret = tree_menu(dic)
            flag = ret

# tree_menu(menu)
# print('hahaha')


# def threeLM(menu):
#     while True:
#         for k in menu:
#             print(k)
#         key = input('input>>>').strip()
#         if key == 'b' or key == 'q':
#             return key
#         elif key in menu.keys() and menu[key]:
#             ret = threeLM(menu[key])
#             if ret == 'q':
#                 return 'q'

# threeLM(menu)




