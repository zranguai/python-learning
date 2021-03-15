"""
### 数据分析：是把隐藏在一些看似杂乱无章的数据背后的信息提炼出来，总结出所研究对象的内在规律
### 数据分析三剑客：Numpy,Pandas,Matplotlib
### NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。
"""
# ### 1. 使用np.array()创建
# + 一维数据创建
import numpy as np
# print(np.array([1, 2, 3, 4, 5]))
# 二维数据创建
# erwei = np.array([[1, 1.2, 3], [4, 5, 'six']])
# print(erwei)
"""
注意：
- numpy默认ndarray的所有元素的类型是相同的
- 如果传进来的列表中包含不同的类型，则统一为同一类型，优先级：str>float>int
"""
# - 使用matplotlib.pyplot获取一个numpy数组，数据来源于一张图片
import matplotlib.pyplot as plt
img_arr = plt.imread('./cat.jpg')
# print(img_arr)
# plt.imshow(img_arr - 100)
print(plt.imshow(img_arr))


