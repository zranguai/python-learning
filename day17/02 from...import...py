"""
    from ... import ...:copy一份过来(对于函数来说，就是引用函数名的内存地址)
    他不是在本文件完全创建一个新的函数，而是创建一个变量read1但是read1指向的函数还是沿用tbjx的read1的内存地址
"""
# from tbjx import name
# from tbjx import read1
# from tbjx import read2
# print(name)
# name = 'haha'
# read1()
# print(globals())

# from tbjx import change
# name = 'alex'
# print(name)
# change()
# from tbjx import name
# print(name)
import sys
print(sys.path)

