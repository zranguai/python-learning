# s = 'alex'
# s2 = s.upper()
# s = s.upper()   # 'alex'没有变，而是指向'alex'的s指向发生了变化
# print(s)

# l1 = [1, 2, 3]
# l1.append(66)
# print(l1)

# dic = {'kk':
#     {
#         'name': 'kk', 'age': 18, 'sex': '男'
#     },
#     'python22': ['1', 2, 3, 4]
# }
# print(dic)

# 字典的创建方式
# 面试会考
# 方式1：
# dic = dict((('one', 1), ('two', 2), ('three', 3)))
# print(dic)
# 方式3：
# dic = dict(one=1, two=2, three=3)
# print(dic)
# 方式3： （官方写法）
# dic = dict({'one': 1, 'two': 2, 'three': 3})
# print(dic)

# 验证字典的合法性: 键应该是不可变数据类型
# dic = {[1, 2, 3]: 'alex', 1:666}
# print(dic)
# dic = {1: '哈哈', 1: '123', 2: '568'}  #键要唯一
# print(dic)
# 字典的增删改查
# dic = {'name': 'haha', 'age': 18, 'hobby_list': ['跑步', '电影']}
# 增：
# 1.直接增加  有则改之，无则增加
# dic['sex'] = '男'
# dic['age'] = 23   #相当于改
# print(dic)
# 2.setdefault()  有则不变，无则增加
# dic.setdefault('hobby')
# dic.setdefault('hobby', '钓鱼')
# print(dic)

# 删
# 1.pop() 按照键去删除键值对  返回值是删除对应的值(重要)
# ret = dic.pop('age')
# ret = dic.pop('ho', '没有此键') #有第二个值不会报错，并且返回第二个值
# print(ret)
# print(dic)
# 2.clear() 清空
# dic.clear()
# print(dic)
# 3. del 按照键删除，没有此键会报错
# del dic['age']
# del dic['age1']
# print(dic)

# 改
# dic['name'] = 'alex'
# print(dic)

# 查
# 1.直接  没有会报错
# print(dic['hobby_list1'])
# 2.get() （重要）可以设置返回值
# l1 = dic.get('hobby_list')
# l1 = dic.get('hobby_list1', '没有此键') # 没有此键时不会报错，并且返回第二个值
# print(l1)
# 三个特殊的
# keys() values() items()
# print(dic.keys())
# 1.可以转化成列表
# print(list(dic.keys()))
# 2.可以遍历循环
# for i in dic.keys():
#     print(i)
# print(dic.values())
# print(dic.items())

# 面试题：一行互换a,b
# a = 18
# b = 12
# a, b = b, a # a, b = 18, 12
# print(a, b)

# 练习客户端合法性
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic['k4'] = 'v4'
# dic.setdefault('k4', 'v4')
# print(dic)
# 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = 'alex'
# print(dic)
# 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic['k3'].append(44)
# print(dic)
# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic['k3'].insert(1, 18)
# print(dic)
