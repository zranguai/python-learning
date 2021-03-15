"""
    json
"""
dic = {'username': 'haha哈', 'age': 22}
import json
# dumps loads 主要用于网络传输，但是也可以读写文件
# 特殊的字符串
# st = json.dumps(dic)
# print(st, type(st))
#
# dic1 = json.loads(st)
# print(dic1, type(dic1))

# l1 = [1, 2, 3, {'name': 'alex'}]
# with open('json文件', mode='w', encoding='utf-8') as f:
#     st = json.dumps(l1)
#     f.write(st)    # 写入文件一定是字符串

# 读取文件还原回去
# with open('json文件', encoding='utf-8') as f1:
#     st = f1.read()
#     l1 = json.loads(st)
#     print(l1, type(l1))

# dump load 只能读写入文件，只能读写入一个数据结构
