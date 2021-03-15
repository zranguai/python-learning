"""
这么做虽然实现了，但是还是有问题的：
1.项目中的这些py文件，肯定会互相引用（只要项目不结束，内存中就一直有core这个模块）
import sys
sys.path.append(r'D:\老男孩python22期代码及笔记\day18\blog\core')
import src
run()
"""
"""
import sys
sys.path.append(r'D:\老男孩python22期代码及笔记\day18\blog\core')
sys.path.append(r'D:\老男孩python22期代码及笔记\day18\blog\conf')
sys.path.append(r'D:\老男孩python22期代码及笔记\day18\blog\db')
sys.path.append(r'D:\老男孩python22期代码及笔记\day18\blog\lib')
sys.path.append(r'D:\老男孩python22期代码及笔记\day18\blog\log')
import src
run()
# 上面肯定是不行，low,不能一个一个添加
"""

"""
# 问题2：此项目是在我的计算机中 他的路径：D:\老男孩python22期代码及笔记\day18\blog 写死了
# 需要动态的获取blog的路径
import sys
# 我直接添加blog的目录
sys.path.append(r'D:\老男孩python22期代码及笔记\day18\blog')
from core import src
# print(sys.path)
run()
"""

# import sys
# import os
# print(__file__)    # 动态的获取本文件的绝对路径 D:/老男孩python22期代码及笔记/day18/blog/bin/starts.py
# print(os.path.dirname(__file__))    # 获取父级的目录 D:/老男孩python22期代码及笔记/day18/blog/bin
# print(os.path.dirname(os.path.dirname(__file__)))  # 获取爷爷级目录 D:/老男孩python22期代码及笔记/day18/blog
###############以上是思路
import os
import sys
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
from core import src

if __name__ == '__main__':
    src.run()