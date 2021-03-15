# super是按照mro的顺序来寻找当前类的下一个类的

# 在py3中不需要传参数,自动就帮我们寻找当前类的mro顺序的下一个类中的同名方法
# 在py2中的新式类中,需要我们主动传递参数super(子类的名字,子类的对象).函数名()
# 这样才能够帮我们调用到这个子类的mro顺序的下一个类中的方法
# 在py2的经典类中,并不支持使用super来找下一个类

# 在D类中找super的func,那么可以这样写 super().func()
# 也可以这样写 super(D,self).func() (并且在py2的新式类中必须这样写)

# 在单继承的程序中，super就是找父类
# class A(object):
#     def func(self):
#         print('A')
# class B(A):
#     def func(self):
#         super().func()
#         print('B')
# class C(A):
#     def func(self):
#         super().func()
#         print('C')
# class D(B,C):
#     def func(self):
#         super().func()    # 默认传当前类的名字，当前类的对象
#         super(D,self).func()
#         print('D')
#
# D().func()


# 默写
class User:
    def __init__(self,name):
        self.name = name
class VIPUser(User):
    def __init__(self,name,level,strat_date,end_date):
        # User.__init__(self,name)    # 可以不继承
        super().__init__(name)              # 推荐的  用super必须要继承  执行父类的同名方法
        # super(VIPUser,self).__init__(name)
        self.level = level
        self.strat_date = strat_date
        self.end_date = end_date


太白 = VIPUser('太白',6,'2019-01-01','2020-01-01')
print(太白.__dict__)


















