# 面向对象的回顾
# 类
# class 类名:
#     静态变量 = '值'
#     def 函数(self):
#         '函数体的内容'
#         pass
# 所有的变量和函数的地址都存储在类的命名空间里

# 对象
    # 对象 = 类名()
# 怎么用
    # 类能做什么用?
        # 1.实例化对象
        # 2.操作静态变量
    # 什么时候是对类中的变量赋值,或者去使用类中的变量
        # 类名.名字 = '值'
        # print(类名.名字)
        # print(对象名.名字) # 如果对象本身没有这个名字
    # 什么时候是对对象中的变量赋值
        # 对象.名字的时候
        # self.名字的时候

# class A:
#     role = []
#     def __init__(self):
#         self.l = []
#     def append(self,obj):
#         self.l.append(obj)
#     def pop(self,index=-1):
#         self.l.pop(index)
# print(A.role)
# a = A()


# class B:
#     def append(self, value):
#         self.l.append(value)
#
# b = B()
# b.l = []
# b.append(10)
# print(b.l)

# 所有的对象调用方法，就看这个对象是哪一个类的方法
# 不要担心类的方法的名字一样

# 写代码的时候,是先有的父类还是先有的子类?
    # 在加载代码的过程中 需要先加载父类 所以父类写在前面
    # 从思考的角度出发 总是先把子类都写完 发现重复的代码 再把重复的代码放到父类中


# 例4
# class A:
#     def func(self):
#         print('a')
#         print(self)
#
# A.func(1)
# class B(A):
#     def func(self):
#         print('b')
#         A.func(self)
#         print(self)
# b = B()
# print(b)
# b.func()     # b,a


# 例6(重要)
# class A:
#     lst = []
#     def __init__(self):
#         self.lst = []
#     def func(self):
#         self.lst.append(1)
# class B(A):
#     def __init__(self):
#         self.lst= []
#     def func(self):
#         self.lst.append(2)
# b = B()
# b.func()
# print(A.lst)  # []
# print(B.lst)  # []



# 栈 队列 默写
# mypickle 仿照这个类写一个myjson(可以dump多次,load多次)
# 作业：把今天的例子内存关系图画出来




















