# properity的应用场景1
from math import pi
class Circle:
    def __init__(self,r):
        self.r = r

    @property   # 把一个方法伪装成一个属性,在调用这个方法的时候不需要加()就可以直接得到返回值
    def area(self):
        return pi * self.r**2

# c1 = Circle(5)
# print(c1.r)
# print(c1.area)
# 变量的属性和方法?
    # 属性 :圆形的半径\圆形的面积
    # 方法 :登录  注册
import time
class Person:
    def __init__(self, name, birth):
        self.birth = birth
        self.name = name
    @property    # 装饰这个方法  不能有参数
    def age(self):
        return time.localtime().tm_year - self.birth

# p = Person('xiaohong', 1998)
# print(p.age)

# property的应用场景2：和私有的属性合作的
# 能看不能改
class User:
    def __init__(self, usr, pwd):
        self.usr = usr
        self.__pwd = pwd
    @property
    def pwd(self):
        return self.__pwd
# alex = User('alex', 'sbsbsb')
# print(alex.pwd)

# property进阶（一般用的比较少）了解
class Goods:
    discount = 0.8
    def __init__(self, name, origin_price):
        self.name = name
        self.__price = origin_price
    @property
    def price(self):
        return self.__price * self.discount
    @price.setter
    def price(self, new_value):    # 你要按照我的要求来改
        self.__price = 10
        # print('调用了',new_value)

# apple = Goods('apple', 5)
# print(apple.price)    # 调用的是被@property装饰的price
# apple.price = 10    # 调用的是被setter装饰的price
# print(apple.price)

# 了解
class Goods:
    discount = 0.8
    def __init__(self,name,origin_price):
        self.name = name
        self.__price = origin_price
    @property
    def price(self):
        return self.__price * self.discount

    @price.setter
    def price(self,new_value):
        if isinstance(new_value,int):
            self.__price = new_value

    @price.deleter
    def price(self):
        del self.__price
apple = Goods('apple',5)
print(apple.price)
apple.price = 'ashkaksk'
del apple.price   # 并不能真的删除什么,只是调用对应的被@price.deleter装饰的方法而已
print(apple.price)








































