# findall***
# search***
import re
# split() 切割
# ret = re.split('\d+', 'alex222hahaha')
# ret = re.split('(\d+)', 'alex222hahaha')
# ret = re.split('\d(\d)\d', 'alex222hahaha')
# print(ret)

# sub()  替换
# ret = re.sub('\d+', 'HH', 'alex123haha456')
# ret = re.sub('\d+', 'HH', 'alex123haha456', 1)
# print(ret)

# subn 替换返回一个元组（第一个参数替换的东西，第二个参数替换的次数）
# ret = re.subn('\d+', 'HH', 'alex123haha456')  # ('alexHHhahaHH', 2)
# print(ret)

# match*  从头找(等同于search前面加个^)
# match 用户输入的内容匹配的时候，要求用户输入11位手机号码，^手机号码正则$
# match('手机号正则$'，'ss')  规定这个字符号必须是什么样的
# search('^手机号正则$'，'ss')  用来寻找是否含有满足条件的子内容
# ret = re.match('\d+', '123evaltaibai456')
# print(ret)
# ret = re.search('^\d+', '123evaltaibai456')
# print(ret)
# print(ret.group())

# 解决findall，search空间/时间问题
# compile**（会先进行预编译，节省代码时间的工具）
#     假如同一个正则表达式要使用多次
#     节省了多次解析同一个正则表达式的时间
#     如果没有重复使用同一个正则，也不能节省时间
# ret = re.compile('\d+')
# res1 = ret.search('alex37176')
# res2 = ret.findall('alex37176')
# print(res1)
# print(res2)

# finditer**  节省空间（迭代器）（在结果特别多时用这个）
# ret = re.finditer('\d+', 'jsdiausd548l521h3a5jsadj')
# print(ret)
# for i in ret:
#     print(i.group())    # i是一个变量
# re.findall('^\d+', '123evaltaibai456')

# 既节省时间有节省空间
# 先compile后finditer
ret = re.compile('\d+')
res = ret.finditer('123evaltaibai456')
for r in res:
    print(r.group())


# 时间/空间
# 列表为什么起始位置从0开始（最简洁）
# 因为0的位置代表起始地址，方便后面元素的地址计算，如果从1开始计算较为复杂


# 写代码注意事项：
# 功能
#   时间：
       # 你要完成一个代码所需要执行的代码行数
       # 你在执行代码的过程中，底层程序是如何工作的
#   空间
    # 是占用了宝贵的内存条资源
    # 影响程序的执行效率
# 用户体验



