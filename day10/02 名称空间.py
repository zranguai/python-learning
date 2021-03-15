# 名称空间：命名空间
# 1.全局名称空间(当前py文件)
# 2.局部名称空间(函数，函数执行时才开辟)（临时名称空间）：
# 3.内置名称空间(builtins.py)：python源码给你提供的一些内置的函数，print(),input()

# 加载顺序：
# 内置名称空间（文件在第一行时内置名称空间就加载进来了）--> 全局名称空间 --> 局部名称空间

# 取值顺序：(就近原则)单向不可逆
# LEGB原则: L:local , E:eclose, G: global, B: builtin
# （从局部找时）局部名称空间 --> 全局名称空间 --> 内置名称空间

# 作用域:
# 两个作用域：
#     全局作用域：内置名称空间 全局名称空间
#     局部作用域：局部名称空间

# 局部作用域可以引用全局作用域的变量（不能改变）

# count = 1
# def func():
#     count += 1
#     print(count)    # UnboundLocalError: local variable 'count' referenced before assignment
# func()

# def func():
#     count = 1
#     def inner():
#         count += 2
#         print(count)    # UnboundLocalError: local variable 'count' referenced before assignment
#     inner()
# func()

# 局部作用域不能改变全局作用域的变量：但python解释器读取到局部作用域时，发现了你对一个变量进行了修改的操作，
# 解释器会认为你在局部已经定义过这个局部变量了，他就从局部找这个局部变量，报错了

# name = '哈哈'
# def func():
#     name = 'alex'
#     print(name)
# func()
# a = 1
# b = 2
# c = 3
