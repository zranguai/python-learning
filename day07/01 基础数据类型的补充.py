# str: 补充的方法练习一遍就行
# s1 = 'taiBAi'
# 1.capitalize() #首字母大写，其余变小写
# print(s1.capitalize())
# 2.swapcase() 大小写翻转
# print(s1.swapcase())
# 3.title() 每个首字母大写（只要是以非字母元素隔开）
# msg = 'he3llo tau bai'
# print(msg.title())
# 4.center() 居中
# s1 = 'barry'
# print(s1.center(20))
# print(s1.center(20, '*'))
# 5.find() 根据元素找到索引，找到就返回，找不到就返回-1
# index()  根据元素找到索引，找到就返回,找不到就报错
# s1 = 'barry'
# print(s1.find('a'))
# print(s1.find('o'))    #-1
# print(s1.find('r'))    #找到第一个就返回
# print(s1.index('a'))
# print(s1.index('o'))

# tuple
# 1.元组中如果只有一个元素，并且没有逗号，那么他不是元组，他与该元素的数据类型一致  ***
# tu1 = (2)
# tu2 = (2,)
# print(type(tu1))
# print(type(tu2))
# 2.count() 计数
# tu = (1, 2, 3, 3, 4, 5, 4, 3)
# print(tu.count(3))
# 3.index() 根据元素找到索引，找到就返回,找不到就报错
# tu = ('haha', 'heihei', 'haha')
# print(tu.index('hahah'))

# list
# l1 = ['哈哈', '呵呵', '嘿嘿']
# 1.count() pass
# 2.index() pass
# 3.sort() 对原列表进行排序 默认从小到大当l1.sort(reverse=True)时，从大到小 **
# l1 = [5, 4, 3, 7, 8, 6, 1, 9]
# l1.sort()
# l1.sort(reverse=True)
# 4.reverse() 反转 **
# l1.reverse()
# print(l1)
# 5. + 列表相加返回一个新的列表
# l1 = [1, 2, 3]
# l2 = ['哈哈', '呵呵', '嘿嘿']
# print(l1 + l2)
# 6.* 列表相乘返回一个新的列表
# l3 = l1 * 3
# print(l3)
# 练习题：将索引为奇数的删除 ***
# l1 = [11, 22, 33, 44, 55]
# for index in range(len(l1)):  #错误
#     if index % 2 == 1:
#         l1.pop(index)
# print(l1)
# 方法1：直接删
# del l1[1::2]
# print(l1)
# 方法2：倒序删
# for index in range(len(l1) - 1, -1, -1):
#     if index % 2 == 1:
#         l1.pop(index)
# print(l1)
# 方法3：利用一个新的空间
# new_l1 = []
# for index in range(len(l1)):  #错误
#     if index % 2 == 0:
#         new_l1.append(l1[index])
# l1 = new_l1
# print(l1)
# 总结：循环一个列表是最好不要改变列表的索引，这样会影响最后结果

# dict
# 1.update()  ***有则覆盖，无则更新
# dic = {'name': '张三', 'age': 18}
# dic.update(hobby='运动', high='175')
# dic.update(name='李四')
# dic.update([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])  #面试会考
# print(dic)
# dic1 = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex","weight":75}
# dic1.update(dic2)
# print(dic1) # {'name': 'alex', 'age': 18, 'sex': 'male', 'weight': 75}
# print(dic2) # {'name': 'alex', 'weight': 75}
# 2.fromkeys() 来自键  #面试会考
# dic = dict.fromkeys('abc', 100)
# dic = dict.fromkeys([1, 2, 3], 100)
# 坑：值公用一个 面试题
# dic = dict.fromkeys([1, 2, 3], [])
# dic[1].append(333)
# print(dic)

# 练习题 将字典中含有‘K’元素的键值对删除
# 循环一个字典时，改变这个字典的大小会报错
# dic = {'k1': '太白', 'k2': 'barry', 'k3': '白白', 'age': 18}
# 法1：报错
# for i in dic:
#     if 'k' in i:
#         dic.pop(i)
# print(dic)
# 法2
# l1 = []
# for key in dic:
#     if 'k' in key:
#         l1.append(key)
# # print(l1)
# for i in l1:
#     dic.pop(i)
# print(dic)
# 法3
# for key in list(dic.keys()):  # ['k1','k2'.'k3']
#     if 'k' in key:
#         dic.pop(key)
# print(dic)

