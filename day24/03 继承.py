
# 猫
# 吃
# 喝
# 睡
# 爬树
# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print(f'{self.name}is eating')
#     def drunk(self):
#         print(f'{self.name}is drunging')
#     def sleep(self):
#         print(f'{self.name}is sleeping')
#     def climp_tree(self):
#         print(f'{self.name}is clamping')

# 狗
# 吃
# 喝
# 睡
# 看家
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f'{self.name}is eating')
#
#     def drunk(self):
#         print(f'{self.name}is drunging')
#
#     def sleep(self):
#         print(f'{self.name}is sleeping')
#     def look_hoom(self):
#         print(f'{self.name}is looking Home')
#
# xiaobai = Cat('小白')
# xiaobai.eat()

# 继承---》需要解决代码的重复
# class A:
#     pass
# class B(A):
#     pass
# B继承A,A是父类，B是子类
# A是父类 基类 超类
# B是子类 派生类
#
# 子类可以使用父类中的：方法 静态变量

class Animal:
    def __init__(self, name):
        self.name = name
        self.blood = 100
        self.wise = 100
    def eat(self):
        print(f'{self.name}is eating')
    def drunk(self):
        print(f'{self.name}is drunging')
    def sleep(self):
        print(f'{self.name}is sleeping')

# class Cat(Animal):
#     def climp_tree(self):
#         print(f'{self.name}is clamping')
# class Dog(Animal):
#     def look_hoom(self):
#         print(f'{self.name}is looking Home')

# xiaobai = Cat('小小白')
# xiaobai.eat()
# xiaobai.climp_tree()
# xiaohei = Dog('小黑')
# xiaohei.drunk()
# 先开辟空间，空间中有一个类指针-->指向Cat
# 调用init,对象在[自己的空间中找init没找到]，到Cat类中找init也没有找到
# 找父类Animal中的init

# 当子类和父类方法重名的时候，我们只使用子类的方法，而不会调用父类的方法



# 子类想要调用父类的方法的同时还想要执行自己的同名方法
# 猫和狗在调用eat的时候即调用自己的也调用父类的
# 在子类的方法中调用父类的方法：父类名.方法名（self）
# 通过Animal.eat(self)
class Cat(Animal):
    # def __init__(self, age):
    #     self.age = 18
    def eat(self):
        self.blood += 100
        Animal.eat(self)
    def climp_tree(self):
        print(f'{self.name}is clamping')
        self.sleep()

class Dog(Animal):
    def eat(self):
        self.wise += 100
        # Animal.eat(self)
    def look_hoom(self):
        print(f'{self.name}is looking Home')

# xiaobai = Cat('小小白')
# xiaohei = Dog('小黑')
# xiaobai.eat()
# xiaobai.climp_tree()
# xiaohei.eat()
# print(xiaobai.__dict__)
# print(xiaohei.__dict__)



# 父类和子类方法的选择:
    # 子类的对象,如果去调用方法
    # 永远优先调用自己的
        # 如果自己有 用自己的
        # 自己没有 用父类的
        # 如果自己有 还想用父类的 : 直接在子类方法中调父类的方法 父类名.方法名(self)

# 思考一:下面代码的输出?(经典面试题)
class Foo:
    def __init__(self):
        self.func()   # 在每一个self调用func的时候,我们不看这句话是在哪里执行,只看self是谁

    def func(self):
        print('in foo')

class Son(Foo):
    def func(self):
        print('in son')
# Son()

# 思考二: 如果想给狗和猫定制个性的属性
class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.blood = 100
        self.waise = 100
    def eat(self):
        print('%s is eating %s'%(self.name,self.food))
    def drink(self):
        print('%s is drinking'%self.name)
    def sleep(self):
        print('%s is sleeping'%self.name)
class Cat(Animal):
    def __init__(self,name,food,eye_color):
        Animal.__init__(self,name,food)    # 调用了父类的初始化,去完成一些通用(重叠)属性的初始化
        self.eye_color = eye_color         # 派生属性

# 猫 : eye_color眼睛的颜色
# 狗 : size型号
# xiaobai = Cat('小白', '猫粮', '蓝色')
# print(xiaobai.__dict__)

# 自己练习狗类
class Dog(Animal):
    def __init__(self, name, food, size):
        Animal.__init__(self, name, food)
        self.size = size

# xiaohhh = Dog('小黑黑', '狗粮', '18码')
# print(xiaohhh.__dict__)


# 单继承
# class D:
#     def func(self):
#         print('in D')
# class C(D):pass
# class A(C):
#     def func(self):
#         print('in A')
# class B(A):pass
# B().func()

# 多继承（java里面不支持多继承）
    # python语言特点：可以在面向对象中支持多继承

class B:
    def func(self):
        print('in B')
class A:
    def func(self):
        print('in C')
class C(B, A):    #(谁离他近，先计算谁)
    pass
C().func()


# 单继承
# 调子类的 : 子类自己有的时候
# 调父类的 : 子类自己没有的时候
# 调子类和父类的 :子类父类都有,在子类中调用父类的
#
# 多继承
# 一个类有多个父类,在调用父类方法的时候,按照继承顺序,先继承的就先寻找










