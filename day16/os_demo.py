"""3
    os模块（operation system）:和操作系统相关的操作封装到该模块中
"""
import os
# 文件操作相关（重命名/删除）
# 1.remove()删除
# os.remove('aa')
# 2.rename()重命名:里面内容不会变
# os.rename('a.txt', 'b.txt')

# 3.删除目录,必须是空目录才能删(不会在回收站中，直接就删除了)
# os.removedirs('aa')

# 4.使用shutil模块可以删除带内容的目录(sh是shell意思)
# import shutil
# shutil.rmtree('aa')

# 和路径相关的操作，被封装到例外一个子模块中：os.path
# 1.dirname() 获取文件父目录
# res = os.path.dirname(r'd:/aaa/bbb/ccc/a.txt')  # 不判断路径是否存在
# print(res)
# 2.basename() 获取文件名
# res = os.path.basename(r'd:/aaa/bbb/ccc/a.txt')
# print(res)
# 3.split() 把文件路径名和文件名切割开,返回一个元组
# res = os.path.split(r'd:/aaa/bbb/ccc/a.txt')
# print(res)
# 4.join() 拼接路径
# res = os.path.join('d:\\', 'aaa', 'bbb', 'c.txt')
# print(res)
# 5.abspath 如果是/开头的路径，默认是在当前盘符下
# 如果不是/开头，默认当前路径
res = os.path.abspath(r'/a/b/c')
res = os.path.abspath(r'a/b/c')
print(res)

# 判断
# 6.isabs() 判断是不是绝对路径
# print(os.path.isabs('d:/a.txt'))  # True
# print(os.path.isabs('a.txt'))  # False
# 7.isdir() 判断是不是目录  (文件不存在False,文件存在但是不是目录False)
# print(os.path.isdir(r'D:\老男孩python22期代码及笔记\day16\aa'))
# 8.exists() 判断文件/目录存在与否
# print(os.path.exists(r'D:\老男孩python22期代码及笔记\day16'))
# 9.isfile() 判断是不是文件(找不到和不是文件都是返回False)
# print(os.path.isfile(r'D:\老男孩python22期代码及笔记\day16\b.txt'))

