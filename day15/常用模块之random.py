"""
random模块
"""
# import random
# 1.random.random():获取[0.0,1.0)的随机浮点数
# ret = random.random()
# print(ret)
# 2.random.randint(a,b):获取[a, b]范围内的一个整数
# print(random.randint(1, 10))
# 3.random.uniform(a, b) :获取[a, b)的随机浮点数(后面的b取不取得到取决于操作系统)
# print(random.uniform(1, 5))
# 4.random.shuffle(x):把参数指定的数据中的元素打乱。参数必须是一个可变的数据类型[列表]（改原数据，没有返回值）
# x = [1, 2, 6, 5, 8]
# random.shuffle()
# print(x)
# 5.random.sample(x, k):从x中随机抽取k个数据，组成一个列表返回
# x = (1, 2, 6, 5, 8)
# l1 = random.sample(x, 3)
# print(l1)
# 通过sample变相实现打乱
# t = (1, 2, 3)
# lst = random.sample(t, len(t))
# print(lst)
