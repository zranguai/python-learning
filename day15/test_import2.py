"""
    导入模块的多种测试
"""
import os
import sys
sys.path.append(os.path.dirname(__file__) + r'\aa')
# 使用import xxx 导入
import my_module

# print(my_module.age)
# 使用from xxx import xx的导入方式(容易参数命名冲突)
# from my_module import age
#     # age = 100
# print(age)

# 使用别名避免命名冲突
# from my_module import age as a
# age = 1000
# print(age)
# print(a)
# 给模块起别名
# import my_module as m
# print(m.age)

# 验证__all__
# from my_module import *
# print(age)
# print(age2)
# print(age3)

