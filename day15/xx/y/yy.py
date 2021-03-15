"""
此模块作为对外引用的入口(从z中导入)
"""

# 相对导入
# from ..z import zz    # 容易向外界暴露zz模块
from ..z.zz import *

# 定义自己的成员
age2 = 888
def f2():
    print('f2f2')