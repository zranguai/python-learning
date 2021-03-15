# 类的成员和命名空间
class A:    # 把所有都放进去时A才指向内存空间
    Country = '中国'    # 静态变量/静态属性 存储从在类的名称空间里# 存的是变量的时候(A.__dict__)是值
    def __init__(self): # 绑定方法 存储从在类的名称空间里
        # self.name = name
        pass
        # self.age = age
        # self.country = country
    def func1(self):    # 存的是函数的时候(A.__dict__)是地址
        print(self)
    def func2(self):
        pass


# print(A.__dict__)
# a = A()    # 类指针，存储类所在的内存地址
# a.func1()    # 等同于 A.func1()    # 类名调用

# a = A('alex', 83, '印度人')
# b = A('wusir', 74, '泰国人')
# a.Country = '日本人'
# print(a.Country)    # 日本人
# print(b.Country)    # 泰国人  # 从对象的命名空间取值
# print(A.Country)    # 中国    # 从类的名称空间取值


# 案例2：
# class A:    # 把所有都放进去时A才指向内存空间
#     Country = '中国'    # 静态变量/静态属性 存储从在类的名称空间里# 存的是变量的时候A.__dict__是值
#     def __init__(self, name, age, country): # 绑定方法 存储从在类的名称空间里
#         self.name = name
#         self.age = age
#         # self.country = country
#     def func1(self):    # 存的是函数的时候A.__dict__是地址
#         print(self)
#     def func2(self):
#         pass

# a = A('alex', 83, '印度人')
# b = A('wusir', 74, '泰国人')
#
# A.Country = '日本人'
# print(a.Country)    # 日本人
# print(b.Country)    # 日本人
# print(A.Country)    # 日本人




# 类中的变量是静态变量
# 对象中的变量只属于对象本身，每个对象都有自己的空间来存储对象的变量
# 当使用对象名去调用某一个属性的时候会优先在自己的空间中寻找，找不到在到类中寻找
# 如果自家没有就引用类的，如果类中也没有就报错
# 对于类来说，类中的变量所有的对象都可以读取的，并且读取的是同一份变量

# 练习题：
# 实现一个类，能够自动统计这个类实例化了多少个对象
# 思路：每个对象改类中的静态变量

class Sum_total:
    count = 0
    def __init__(self):
        Sum_total.count += 1

# s1 = Sum_total()
# s1 = Sum_total()
# s1 = Sum_total()
#
# print(s1.count)

# 类中静态变量的用处（重要）
# 如果一个变量 是所有的对象共享的值，那么这个变量应该被定义成静态变量
# 所有和静态变量相关的增删改查都应该使用类名来修改
# 而不是使用对象名直接修改静态变量











