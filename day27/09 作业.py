# 1.面向对象的私有成员有什么？

# 2.如何设置面向对象的类方法与静态方法，类方法静态方法有什么用？

# 3.面向对象中属性是什么？有什么作用？
# class A:
#     @property  # 将方法伪装成属性，看起来更合理 把一个方法变成一个静态属性
#     def eat(self):
#         print("test")  # obj.eat
#
#     @eat.setter
#     def eat(self, food):
#         print("赋值之前执行我")  # obj.eat = 777
#
#     @eat.deleter
#     def eat(self):
#         print("删除之前执行我")
# a = A()
# a.eat
# a.eat = 666
# del a.eat
# 4.isinstance与issubclass的作用是什么？
# isinstance：判断是不是类的实例  issubclass：判断是不是子类或者孙子类
# 5.看代码写结果：
# class A:
#     a = 1
#     b = 2
#     def __init__(self):
#         c = 3
#
# obj1 = A()
# obj2 = A()
# obj1.a = 3
# obj2.b = obj2.b + 3
# print(A.a)    # 1
# print(obj1.b) # 2
# print(obj2.c) # 报错
# 6.看代码写结果：
# class Person:
#     name = 'aaa'
#
# p1 = Person()
# p2 = Person()
# p1.name = 'bbb'
# print(p1.name)    # bbb
# print(p2.name)    # aaa
# print(Person.name)# aaa
# 7.看代码写结果：
# class Person:
#     name = []
#
# p1 = Person()
# p2 = Person()
# p1.name.append(1)
# print(p1.name)    # [1]
# print(p2.name)    # [1]
# print(Person.name)# [1]
# 8.看代码写结果：
# class A:
#
#     def __init__(self):
#         self.__func()
#
#     def __func(self):
#         print('in A __func')
#
#
# class B(A):
#
#     def __func(self):
#         print('in B __func')
#
#
# obj = B()    # in A __func
# 9.看代码写结果：
# class Init(object):
#
#     def __init__(self, value):
#         self.val = value
#
#
# class Add2(Init):
#
#     def __init__(self, val):
#         super(Add2, self).__init__(val)
#         self.val += 2
#
#
# class Mul5(Init):
#
#     def __init__(self, val):
#         super(Mul5, self).__init__(val)
#         self.val *= 5
#
#
# class Pro(Mul5, Add2):
#     pass
#
#
# class Iner(Pro):
#     csup = super(Pro)
#
#     def __init__(self, val):
#         self.csup.__init__(val)
#         self.val += 1
#
#
# # 虽然没有见过这样的写法，其实本质是一样的，可以按照你的猜想来。
# p = Iner(5)
# print(p.val)    # 36
#
# 10.请按下列要求，完成一个商品类。
#
    # 封装商品名，商品原价，以及折扣价。
    # 实现一个获取商品实际价格的方法price。
    # 接下来完成三个方法，利用属性组合完成下列需求：
        # 利用属性property将此price方法伪装成属性。
        # 利用setter装饰器装饰并实现修改商品原价。
        # 利用deltter装饰器装饰并真正删除原价属性。
# class Goods:
#     def __init__(self, name, price, discount_price):
#         self.__name = name
#         self.__price = price
#         self.__discount_price = discount_price
#     def get_price(self):
#         return self.__discount_price
#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self, new_price):
#         self.__price = new_price
#     @price.deleter
#     def price(self):
#         del self.__price
#
# goods = Goods('apple', 15, 10)
# print(goods.get_price())
# print(goods.price)
# goods.price = 100
# print(goods.price)
# del goods.price
# print(goods.__dict__)













