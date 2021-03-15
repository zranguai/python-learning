"""2
    datetime模块
    封装了一些和日期，时间相关的类
    date
    time
    datetime
    timedelta
"""
import datetime
# date类（包含年月日）
# d = datetime.date(2010, 10, 10)
# print(d)
# 获取date类的各个属性
# print(d.year)
# print(d.month)
# print(d.day)

# time类（包含时分秒）
# t = datetime.time(10, 48, 59)
# print(t)
# time类的属性
# print(t.hour)
# print(t.minute)
# print(t.second)

# datetime类（主要用于计算）
# dt = datetime.datetime(2010, 11, 11, 11, 11, 11)
# print(dt)
# 可以获取年月日时分秒这6个属性
# datetime中的类，主要用于数学计算的

# timedelta(时间变化量)
# td = datetime.timedelta(days=2)
# print(td)
# 参与数学运算
# 创建时间对象
# date,datetime,timedelta(只能这三位参与计算)
# d = datetime.date(2010, 10, 10)
# res = d + td
# print(res)

# 时间变化量的计算是否会产生进位？会！！
# t = datetime.datetime(2010, 10, 10, 10, 10, 00)
# td = datetime.timedelta(seconds=4)
# res = t - td
# print(res)


# 练习客户端合法性：计算某一年的二月份有多少天
# 1.普通算法：根据年份计算是否是闰年，是29天否28天
# 2.用datetime模块
# 思路：首先创建指定模块的3月1号，然后往前走一天
year = int(input('输入年份'))
d = datetime.date(year, 3, 1)
td = datetime.timedelta(days=1)
res = d - td    # res的类型与d的类型同[和时间段进行运算的结果，类型和例外一个操作数保持一致]
print(res.day)
