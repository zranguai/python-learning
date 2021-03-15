# object类 类祖宗
# 所有在python3当中的类都是继承object类的
# object中有init
# 所有的类都默认的继承object

# #__base__只查看从左到右继承的第一个子类，__bases__则是查看所有继承的父类
class A:
    pass
class C:
    pass

class B(A, C):
    pass
# print(B.__bases__)
# print(A.__bases__)


# isinstance(判断数据类型)  判断类与类之间的继承关系的
# type(查看数据类型)
# a = 3
# print(isinstance(a, int))

# class Cat:
#     pass
# xiaobai = Cat()
# print(id(type(xiaobai)))
# print(id(Cat))
# print(type(xiaobai) is Cat)

# 绑定方法和普通函数
# 方法与类的区别不在于是否写在类里面，而是在于谁去调用它
# from types import FunctionType, MethodType
# FunctionType: 判断是否是函数
# MethodType： 判断是否是方法
# class A:
#     def func(self):
#         print('in func')
#
# print(A.func)  # 函数  用类名调用时函数
# a = A()
# print(a.func)  # 方法  用对象调用是方法
# print(isinstance(a.func, FunctionType))
# print(isinstance(a.func, MethodType))


class A:
    role = '法师'

class B:pass

class C(B, A):pass

print(A.__base__)
print(C.__bases__)
print(A.__dict__)
print(A.__name__)
print(B.__class__)    # 查看类的类型（大部分都是type类型）
print(C.__module__)   #  类定义所在的模块

# __doc__  类的文档字符串  查看注释
def func():
    '''
    这个函数主要是用来卖萌
    :return:
    '''
    pass

print(func.__doc__)

class Cat:
    '''
    这个类是用来描述游戏中的猫咪角色
    '''
    pass
print(Cat.__doc__)


















