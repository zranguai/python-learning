# 1.
# 看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
# class Foo(object):
#     a1 = 1
#
#     def __init__(self, num):
#         self.num = num
#
#     def show_data(self):
#         print(self.num + self.a1)
#
#
# obj1 = Foo(666)
# obj2 = Foo(999)
# print(obj1.num)    # 666
# print(obj1.a1)    # 1
# #
# obj1.num = 18
# obj1.a1 = 99
# #
# print(obj1.num)    # 18
# print(obj1.a1)     # 99
#
# print(obj2.a1)    # 99    (错误该方法时在obj2上面添加了a1属性)
# print(obj1.__dict__)
# print(obj2.num)   # 999
# print(obj2.num)   # 999
# print(Foo.a1)     # 1
# print(obj1.a1)    # 99
#
#
# 2.
# 看代码写结果，注意返回值。
#
#
#
# class Foo(object):
#
#     def f1(self):
#         return 999
#
#     def f2(self):
#         v = self.f1()  # 999
#         print('f2')
#         return v
#
#     def f3(self):
#         print('f3')
#         return self.f2()
#
#     def run(self):
#         result = self.f3()  # self.f2()
#         print(result)
#
#
# obj = Foo()
# v1 = obj.run()  # f3 f2  999 None
# print(v1)

#
# 3.
# 看代码写结果
#
#
#
class Foo(object):
    def __init__(self, num):
        self.num = num


v1 = [Foo for i in range(10)]
v2 = [Foo(5) for i in range(10)]
v3 = [Foo(i).num for i in range(10)]

# print(v1)    #[<class '__main__.Foo'>10个]
# print(v2)  # [5,5,5,5,5,5,5,5,5,5](错误10个相同地址)
# print(v3)  # [0,1,2,3,4,5,6,7,8,9]（错误10个不同地址）
#
# 4.
# 看代码写结果
#
#
#
# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
# for item in config_obj_list:
#     print(item.num)    # 1 2 3

#
# 5.
# 看代码写结果：
#
#
#
# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
# for item in config_obj_list:
#     item.changelist(666)    # 1 666 2 666 3 666

#
# 6.
# 看代码写结果：

# class Department(object):
#     def __init__(self, title):
#         self.title = title
#
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
#
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)
# p2 = Person('alex', 18, d1)
# p3 = Person('安安', 19, d2)
#
# print(p1.name)    # 武沛齐
# print(p2.age)    # 18
# print(p3.depart)    # 地址
# print(p3.depart.title)    # 销售部

# 7.
# 看代码写结果：
#

# class Department(object):
#     def __init__(self, title):
#         self.title = title
#
#
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
#
#     def message(self):
#         msg = "我是%s,年龄%s,属于%s" % (self.name, self.age, self.depart.title)
#         print(msg)
#
#
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)
# p2 = Person('alex', 18, d1)
# p1.message()    # 我是武沛齐年龄18属于人事部
# p2.message()    # 我是alex今年18属于人事部

# 8.
# 看代码写结果：

# class A:
#     def f1(self):
#         print('in A f1')
# class B(A):
#     def f1(self):
#         print('in B f1')
# class C(A):
#     def f1(self):
#         print('in C f1')
# class D(B, C):
#     def f1(self):
#         # super().f1()
#         super(C, self).f1()    # super方法有参数问题：1.参数是自己本身，调用同super(),2.参数是其他的子类，按照mro顺序调用子类的上一个方法
#         print('in D f1')
# obj = D()
# print(D.mro())
# obj.f1()    # in B f1    in D f1
#
#
# 9.
# 看代码写结果：

# class A:
#     def f1(self):
#         print('in A f1')
#
#
# class B(A):
#     def f1(self):
#         super().f1()
#         print('in B f1')
#
#
# class C(A):
#     def f1(self):
#         print('in C f1')
#
#
# class D(B, C):
#     def f1(self):
#         super().f1()
#         print('in D f1')
#
#
# obj = D()
# obj.f1()    # in C f1  in B f1  in D f1

# 10.程序设计题：
# 运用类完成一个扑克牌类(无大小王)的小游戏：
# 用户需要输入用户名，以下为用户可选选项:
#     1. 洗牌
#     2. 随机抽取一张
#     3. 指定抽取一张
#     4. 从小到大排序
#     5. 退出
# 1. 洗牌：每次执行的结果顺序随机。
# 2. 随机抽取一张：显示结果为：太白金星您随机抽取的牌为：黑桃K
# 3. 指定抽取一张：
#     用户输入序号（1~52）
#     比如输入5，显示结果为：太白金星您抽取的第5张牌为：黑桃A
# 4. 将此牌从小到大显示出来。A -> 2 -> 3 .......-> K
#
# 提供思路：
#     52张牌可以放置一个容器中。
#     用户名，以及盛放牌的容器可以封装到对象属性中。
import random
class Poke:
    list1 = ['A'] + [i for i in range(2, 11)] + ['J', 'Q', "K"]
    def __init__(self):
        pass
    def shuffle_(self):
        random.shuffle(self.lst)
        print(self.lst)
        self.main(self.lst)
    def extract_random(self):
        choose = random.choice(lst)
        print(f'你抽走的牌为{choose}')
        self.lst.remove(choose)
        self.main(self.lst)
    def extract(self):    # 指定抽走一张
        extract_detail = input('您想要抽走那一张')
        if extract_detail in self.lst:
            print(f'你抽走了{extract_detail}')
            self.lst.remove(extract_detail)
        else:
            print('您抽的牌已经被抽走了')
        self.main(self.lst)
    def sort_(self):    # ?????
        self.lst = sorted(self.lst, key=lambda x:self.lst.index(str(x)[2:]))
        print(self.lst)
        self.main(self.lst)
    def main(self, list = []):
        msg = """
            1. 洗牌
            2. 随机抽取一张
            3. 指定抽取一张
            4. 从小到大排序
            5. 退出
        """
        print(msg)
        num = int(input('请输入你选择的序号'))
        if num in [1, 2, 3, 4]:
            l1 = [self.shuffle_, self.extract_random, self.extract, self.sort_]
            l1[num - 1]()
        else:
            quit()


name = input('请输入名字')
poke = Poke()
poke.name = name

list2 = ['黑桃', '红桃', '梅花', '方片']
lst = []
for i in list2:
    for j in poke.list1:
        lst.append(i + str(j))
poke.lst = lst
poke.main(lst)

