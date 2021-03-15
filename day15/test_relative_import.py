"""
测试相对导入
"""
import os
import sys
# 把项目所在的父路径加到sys.path中(如果项目中使用了相对导入，就必须要从项目的根目录进行导入)
sys.path.append(os.path.dirname(__file__))

from xx.y import yy
print(yy.age2)

# print(yy.zz.age)
print(yy.age)
yy.f()