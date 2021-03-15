"""4
    sys模块：和python解释器相关的操作
"""
import sys
# 1.sys.argv  获取命令行方式运行的脚本后面的参数
# 用处：可以在用脚本方式运行时获取其参数，进行一些运算
# print("脚本名", sys.argv[0])    # 第0个脚本名
# print("第1个参数", sys.argv[1])    # 第1个参数
# print(type(sys.argv[1]))    # str

# 2.sys.path 解释器寻找模块的路径

# sys.setrecursionlimit(limit) 设置递归的最大次数

# 3.sys.modules:返回系统已经加载的模块，以字典方式返回
# 常用来作为是否从新加载一个模块的判断依据
# (python解释器在启动时会自动加载一些模块到内存中，可以使用sys.modules查看)
print(sys.modules)


