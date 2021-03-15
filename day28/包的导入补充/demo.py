# import glance
# 导入一个包（文件加）相当于执行了这个包下的__init__文件
# 并不是相当于把这个包下的所有文件都导入进来了
# print(glance)

# 想要直接导入某个包（文件夹）下的文件
# 方式1：import as 语句
# import glance.api.policy as policy
# policy.get()

# 方式2：
# from glance.api import policy    # from...import...的import后面必须是明确的文件或方法
# policy.get()

# 方式3：
# from glance.api.policy import get
# get()


# 进阶：(相对导入的文件是不能够直接运行的)
# sys.path的第一个元素总是你当前执行的这个文件的父目录
import glance
glance.api.policy.get()


import json
# 当你需要写一个功能
# 这个功能不是直接运行的,而是被别人导入之后使用的,这种情况如果你的这个独立功能形成文件夹
# 文件夹内的所有文件都需要使用相对导入

# 但是如果我们自己开发一个项目,这个项目有一些文件是需要直接运行的,这种情况下不适合用相对导入
# 适合用绝对导入

# https://www.cnblogs.com/Eva-J/articles/7292109.html#_label2

# 选课系统没看


















