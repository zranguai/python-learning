""""+
    自定义模块
    什么是模块：模块的本质就是.py文件，封装语句的最小单位
    模块中出现的变量，for循环，if结构，函数定义...称为模块成员

    模块的运行方式：
    脚本运行：直接用解释器执行，或者pycharm中右键运行
    模块方式：被其他的模块导入。为导入它的模块提供资源（变量，函数定义，类定义等）
"""

"""+
 第一次导入模块执行三件事:
     1.创建一个以模块名命名的名称空间。
     2.执行这个名称空间（即导入的模块）里面的代码。
     3.通过此模块名. 的方式引用该模块里面的内容（变量，函数名，类名等）
     [ps：重复导入会直接引用内存中已经加载好的结果]
"""
# 可执行语句
a = 1
# print(a)
#
# for i in range(3):
#     print(i)
# 函数定义：

def foo():
    print('hello nnn')
""" +
    python中提供一种可以判断自定义模块是属于开发阶段还是使用阶段:
    __name__:1.脚本方式运行，固定的字符串：__name__
             2.已导入方式运行时，就是本模块的名字
# print(__name__)

"""

# 定义一个函数，包含测试语句(写模块之前先写这个)
# def main():
#     print(a)
#     for i in range(3):
#         print(i)
#     foo()
#
# if __name__ == '__main__':
#     main()


""" +
系统导入模块的路径：
   1.内存中：如果之前成功导入过某个模块，直接使用已经存在的模块
        # ps：python解释器在启动时会自动加载一些模块到内存中，可以使用sys.modules查看
        import sys
        print(sys.modules)
   2.内置路径中：在安装路径下:lib 
   （PYTHONPATH：import时寻找模块的路径）[一般不用]
   3.sys.path: 是一个路径的列表
如果三个都找不到，就报错
"""

# __file__  # 当前文件的绝对路径
""" + 
获取绝对路径：
    import sys
    sys.path.append(r'D:\老男孩python22期代码及笔记\day15\aa')  # r防止转义
"""

""" + 
获取相对路径：
    os.path.dirname():获取某个路径的父路径。通常用于获取当前模块的相对路径
    import sys
    import os
    sys.path.append(os.path.dirname(__file__) + r'\aa')
"""

"""
导入模块的多种方式：+
    1.import xxx:导入一个模块的所有成员
    2.import aaa,bbb: 一次性导入多个模块的成员（不推荐这种写法，分开写）
    3.from xxx import a:从某个模块中导入指定的成员（好处：节省内存空间）
    4.from xxx import a,b,c:从某个模块中导入多个成员
    5.from xxx import *:从模块中导入所有成员
"""
""" + 
1.import xxx和2.from xxx import *的区别？
    第一种方式在使用其中成员时，必须使用模块名作为前缀，不易产生命名冲突
    第二种方式在使用其中成员时，不用使用模块名作为前缀，直接使用成员名即可，容易参数命名冲突
"""

"""
怎样解决名称冲突的问题？
    1.改用import xxx 这种方式导入
    2.自己避免使用同名
    3..使用别名解决冲突 
        A:给成员取别名from xxx import a as b (将a改别名为b)
        B:给模块起别名 import xxx as m (给模块xxx取别名m)
"""

""" +
from xxx import * 控制成员被导入：
    默认情况下，所有的成员都会被导入
    __all__是一个列表(只针对from xxx import * 起作用)，用于表示本模块可以被外界使用的成员，元素是成员名的字符串
    __all__ = ['name', 'read1',]
"""

""" + 
相对导入：
    针对某个项目中的不同模块之间进行导入，称为相对导入
    只有一种格式：
    from 相对路径 import xxx
    相对路径：. 表示当前的路径 .. 表示的是父路径 ... 表示的是父路径的父路径
"""
# ps：python解释器在启动时会自动加载一些模块到内存中，可以使用sys.modules查看
import sys
print(sys.modules)