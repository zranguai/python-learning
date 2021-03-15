"""6
    pickle模块：
    序列化过程：将python中的所有数据类型转化成字节串。
    反序列化过程：将字节串转化成python中数据类型
"""

import pickle
# bys = pickle.dumps([1, 2, 3])
# print(type(bys))    # <class 'bytes'>
# print(bys)
# 保存了元组的数据类型
# bys = pickle.dumps((1, 2, 3))
# print(type(bys))    # <class 'bytes'>

#
# res = pickle.loads(bys)
# print(type(res))

#
# bys = pickle.dumps(set('abc'))
# print(type(bys))    # <class 'bytes'>
#
# res = pickle.loads(bys)
# print(type(res))

# 把pickle序列化内容写入到文件中(可以实现多次写多次读)
# with open('c.txt', mode='ab') as f:
#     pickle.dump([1, 2, 3], f)
#     pickle.dump([1, 2, 3], f)
#     pickle.dump([1, 2, 3], f)
#     pickle.dump([1, 2, 3], f)
# 从文件中反序列化pickle数据
# with open('c.txt', mode='rb') as f1:
#     for i in range(5):
#         res = pickle.load(f1)
#         print(res)

# pickle常用场景：和json一样，一次性写入，一次性读取


"""
json与pickle的比较：
    json:
    1.不是所有的数据类型都可以序列化，他的结果是字符串
    2.不能多次对同一个文件序列化
    3.json数据可以跨语言
    pickle:
    1.所有python类型都能序列化，结果是字节串
    2.可以多次对同一个文件序列化
    3。不可以跨语言
"""