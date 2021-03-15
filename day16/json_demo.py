"""5
    json模块：javascript Object Notation
    已经成为了一种简单数据交互格式(不完全的序列化)
"""
"""
    序列化：将内存中的数据，转换成字节串，用以保存在文件或通过网络传输
    反序列化：从文件中，网络中获取的数据，转换成内存中原来的数据类型
"""
 # 用于网络传输(内存)：dumps、loads
 # 用于文件写读：dump、load
# json:将数据转换成字符串，用于存储或网络传输（set类型不可以序列化）
import json
# s = json.dumps([1, 2, 3])    # 把指定的对象转换成json格式的字符串
# print(type(s))
# 元组序列化后转换成列表

# 将json结果写到文件中
# with open('a.txt', mode='wt', encoding='utf-8') as f1:
#     json.dump([1, 2, 3], f1)

# 反序列化
# res = json.dumps([1, 2, 3])
# lst = json.loads(res)
# print(type(lst))
# 元组反序列化会变成列表

# 从文件中反序列化
# with open('a.txt', encoding='utf-8') as f1:
#     res = json.load(f1)
#     print(type(res))


# 总结：json
# json.dumps(obj)
# json.dump(obj, f)
# json.loads(s)
# json.load（f）

# 把需要序列化的对象，通过多次序列化的方式，用文件write方法，把多次序列化后的json字符串写到文件中
# with open('json.txt', mode='at', encoding='utf-8') as f:
#     f.write(json.dumps([1, 2, 3]) + '\n')
#     f.write(json.dumps([4, 5, 6]) + '\n')

# 分次反序列化回来
with open('json.txt', mode='rt', encoding='utf-8') as f:
    res = json.loads(f.readline().strip())
    print(res)
    res2 = json.loads(f.readline().strip())
    print(res2)
