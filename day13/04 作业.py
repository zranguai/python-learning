# 用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# name = ['oldboy','alex','wusir']
# ret = map(lambda name: name + "_sb", name)
# print(list(ret))
# 用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
# l = [{'name': 'alex'}, {'name': 'y'}]
# ret = map(lambda nam: nam['name']+'sb', l)
# print(list(ret))
# 用filter来处理,得到股票价格大于20的股票名字
#
# shares = {
#     'IBM': 36.6,
#     'Lenovo': 23.2,
#     'oldboy': 21.2,
#     'ocean': 10.2,
# }
# def func(a):
#     return shares[a] > 20
# ret = filter(func,shares)    # 循环的是字典的键，比较的是字典的值
# print(list(ret))
# 有下面字典，得到购买每只股票的总价格，并放在一个迭代器中结果：list一下[9110.0, 27161.0,......]
#
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 21.09},
# {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# ret = map(lambda a: a['shares'] * a['price'], portfolio)
# print(list(ret))
# 还是上面的字典，用filter过滤出单价大于100的股票。
# def func(a):
#     return a['price'] > 100
# ret = filter(func, portfolio)
# print(list(ret))
# 有下列三种数据类型，
#
l1 = [1,2,3,4,5,6]
l2 = ['oldboy','alex','wusir','太白','日天']
tu = ('**','***','****','*******')
# ​写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）
# [(3, 'wusir', '****'), (4, '太白', '*******')]这样的数据。
# l11 = list(filter(lambda a: a > 2, l1))
# l22 = l2[2:]
# tu1 = list(filter(lambda i: len(i) > 3, tu))
# ret = zip(l11,l22,tu1)
# print(list(ret))
# ret = filter(lambda x: x[0]>2 and len(x[-1]) >= 4,zip(l1, l2, tu))
# print(list(ret))
# ​	7. 有如下数据类型(实战题)：

l1 = [{'sales_volumn': 0},
{'sales_volumn': 108},
{'sales_volumn': 337},
{'sales_volumn': 475},
{'sales_volumn': 396},
{'sales_volumn': 172},
{'sales_volumn': 9},
{'sales_volumn': 58},
{'sales_volumn': 272},
{'sales_volumn': 456},
{'sales_volumn': 440},
{'sales_volumn': 239}]
#
# 将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
# ret = map(lambda a: a['sales_volumn'], l1)
# l2 = sorted(list(ret))
# l3 = ['sales_volumn'] * len(l2)
# l4 = zip(l3, l2)
# l5 = []
# for i in list(l4):
#     dic1 = {}
#     dic1['sales_volumn'] = i[1]
#     l5.append(dic1)
# print(l5)
# print(list(l4))
# print(sorted(l1, key=lambda x: x['sales_volumn']))
# 求结果(面试题)
# def func():
#     return 6
#
# v = [lambda :x for x in range(10)]
# [function 432423, function 65654, function 756767,.......]
# print(v)    # 函数地址
# print(v[0])    # 地址
# print(v[0]())    # 6  错误
# 求结果(面试题)
v = (lambda: x for x in range(10))    # x=9
# print(v)    # 地址
# print(v[0])    # 错误  迭代器对象没有下标
# print(v[0]())    # (错误)
# print(next(v))    # 下一个地址
# print(next(v)())  # 1
# print(str(100), type(str(100)))   # 100
# list(map(str,[1,2,3,4,5,6,7,8,9]))  输出是什么? # (面试题)
# print(list(map(str,[1,2,3,4,5,6,7,8,9])))
# 写一个函数完成三次登陆功能：
# 用户的用户名密码从一个文件register中取出。
# register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
# 完成三次验证，三次验证不成功则登录失败，登录失败返回False。
# 登陆成功返回True。
#
# dic1 = {}
# count = 1
# with open('register', mode='r', encoding='utf-8') as f1:
#     content = f1.readlines()
#     for i in content:
#        l1 = i.split('|')
#        l2 = l1[1].replace('\n', '')
#        dic1[l1[0]] = l2
# print(dic1)
# def log_in(name, pwd):
#         if name in dic1.keys() and pwd in dic1.values():
#             print('恭喜你输入正确')
#             return True
# def inp():
#     name1 = input('请输入姓名')
#     pwd1 = input('请输入密码')
#     return name1, pwd1
# while True:
#     name1, pwd1 = inp()
#     print(name1,pwd1)
#     if count == 3:
#         print('您的次数已经用完')
#         break
#     elif log_in(name1, pwd1):
#         print('输入正确啦')
#         break
#     else:
#         count += 1
#         print(f'你剩下的机会还有{4 - count}次')

# 求结果：（面试题，比较难）
# def num():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in num()])
