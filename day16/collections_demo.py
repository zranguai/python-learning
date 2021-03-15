"""8
    collections模块：常用的容器类
    namedtuple():命名元组
    defaultdict():默认值字典
    Counter():计数器
"""
# 1.namedtuple()
# from collections import namedtuple
# Rectangle = namedtuple('rectangle_class', ['x', 'y'])
# r = Rectangle(10, 15)
# # 通过属性访问元组的元素
# print(r.x)
# print(r.y)
# # 通过索引方式访问元组元素
# print(r[0])
# print(r[1])

# 2.defaultdict()  这里int是工厂函数（可以自定义）
# from collections import defaultdict
# d = defaultdict(int, name='andy', age=10)
# print(d['name'])
# print(d['age'])
# print(d['addr'])    # {'addr': 0}也会被添加

# 自定义函数充当第一个函数，要求：不能有参数
# def f():
#     return 'hahaha'
# d = defaultdict(f, name='andy', age=10)
# print(d['addr'])

# 3.Counter:计数器，参数未可哈希数据
from collections import Counter
c = Counter('asdasaaaasds')
print(c)
# 返回前几名
print(c.most_common(2))
