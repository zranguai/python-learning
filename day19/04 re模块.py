import re
# ret = re.findall('\d+', '19sda256984as57sd40')
# print(ret)
# ret1 = re.search('\d+', 'sda256984as57sd40')  # 找一个就返回
# print(ret1)    # 变量
# print(ret1.group())

# 预习一个现象并找到答案--分组有关系
# findall 还是按照完整的正则进行匹配，总是只显示括号里匹配到的内容
# ret = re.findall('9(\d)\d', '1925sda256984as57sd40')
# print(ret)

# search 还是按照完整的正则进行匹配，显示也显示匹配到的第一个内容，但是我们可以通过给group方法传参数
# 来获取具体分组的内容
# ret1 = re.search('9(\d)(\d)', 'sda25698425as57sd40')  # 找一个就返回
# print(ret1)    # 变量
# if ret1:
#     print(ret1.group())
#     print(ret1.group(1))
#     print(ret1.group(2))



# findall
#     取所有符合条件的，优先显示分组中的
# search 只取第一个符合条件的，没有优先显示这件事
#     得到的结果是一个变量
#         变量.group()的结果完全和变量.group(0)的结果一致
#         变量.group(n)的形式来指定获取第n个分组中匹配到的内容

# 为什么在search中不需要分组优先，而在findall中需要？

# 加上括号 是为了对真正需要的内容进行提取
# findall
# ret = re.findall('<\w+>(\w+)</\w+>','<h1>askhasd256878</h1>')
# print(ret)

# search
# ret = re.search('(<\w+>)(\w+)(</\w+>)','<h1>askhasd256878</h1>')
# print(ret.group())
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(3))

# 为什么要用分组，以及findall的分组优先到底有什么好处
exp = '2-3*(5+6)'
# a+b 或者是a-b并且计算他们的结果
# ret = re.search('\d[+]\d', exp)
# print(ret)
# print(ret.group())
# a, b = ret.group().split('+')
# print(int(a)+int(b))

# ret = re.search('(\d)[+](\d)', exp)
# print(ret)
# print(ret.group(1))
# print(ret.group(2))
# print(int(ret.group(1)) + int(ret.group(2)))

# with open('douban.html', encoding='utf-8') as f:
#     content = f.read()
# ret = re.findall('<span class="title">(.*?)</span>(?:\s*<span class="title">.*?</span>)?', content, flags=re.S)
# print(ret)
# print(len(ret))

# 如果我们要查找的内容在一个复杂的环境中
# 我们要查的内容并没有一个突出的 与众不同的特点 甚至会和不需要的杂乱的数据混合在一起
# 这个时候我们就需要把所有的数据都统计出来,然后对这个数据进行筛选,把我们真正需要的数据对应的正则表达式用()圈起来
# 这样我们就可以筛选出真正需要的数据了

# ret = re.findall('1(?:\d)(\d)', '123')    # ?:取消分组优先
# print(ret)

# 什么是爬虫
    # 通过代码获取到一个网页的源码
    # 要的是源码中嵌着的网页的内容 ---正则表达式

# 分组和findall的现象
    # 为什么要用分组
        # 把想要的内容放在分组里
# 如何取消分组优先
    # 如果再写正则的时候由于不得已的原因，导致不要的内容也得写到分组里
    # （?:）取消这个分组的优先显示

