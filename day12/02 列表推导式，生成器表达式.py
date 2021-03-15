# 列表推导式：
# 用一行代码构建一个比较复杂有规律的列表

# l1 = [i for i in range(1, 11)]
# print(l1)

# 循环模式：[变量（加工后的变量）for 变量 in iterable]
# 筛选模式：[变量（加工后的变量）for 变量 in iterable if 条件]


# 练习题：循环模式
# 将10以内所有整数的平方写入列表。
# l1 = [i**2 for i in range(1, 11)]
# print(l1)
# 100以内所有的偶数写入列表.
# l1 = [i for i in range(0, 101, 2)]
# print(l1)
# 从python1期到python100期写入列表lst
# l1 = [f'python{i}期' for i in range(1, 101)]
# print(l1)



# 筛选模式：[变量（加工后的变量）for 变量 in iterable if 条件]
# 30以内能被3整除的数
# l1 = [i for i in range(1, 31) if i % 3 == 0]
# print(l1)

# 练习题：过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# l = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
# l2 = [i.upper() for i in l if len(i) > 3]
# print(l2)
# 练习题：找到嵌套列表中名字含有两个‘e’的所有名字（有难度）
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
# l1 = []
# for i in names:
#     for j in i:
#         if j.count('e') == 2:
#             l1.append(j)
# print(l1)
# 改进：多重循环列表推导式：
# l1 = [j for i in names for j in i if j.count('e') == 2]
# print(l1)


# 生成器表达式
# 与列表推导式的写法几乎一摸一样，也有循环模式，筛选模式，多层循环构建，写法上[]换成()
# print((i for i in range(1, 11)))
# obj = (i for i in range(1, 11))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# for i in obj:    # 一个可迭代对象都能够for循环，更别说迭代器了
#     print(i)

# 总结：
# 列表推导式：
# 缺点：
# 1. 有毒，列表推导式只能构建比较复杂并且有规律的列表（不要太着迷）
# 2.超过三层循环才能构造成功的，就不建议用列表推导式
# 3.查找模式(debug模式)不行
# 优点：
# 一行构建，简单
# 装逼


# # 练习题：构建一个列表：[2,3,4,5,6,7,8,9,10,'j','Q','K','A']
# l1 = [i for i in range(2, 11)] + list('JQKA')
# print(l1)

# 列表推导式域生成器表达式区别
# 1.写法上： []/()
# 2.iterable/iterator


# 字典推导式
# lst1 = ['jay', 'jj', 'meet']
# lst2 = ['周杰伦', '林俊杰', '郭宝元']
# dic = {lst1[i]: lst2[i] for i in range(len(lst1))}
# print(dic)
# 集合推导式
# print({i for i in range(1, 41)})
