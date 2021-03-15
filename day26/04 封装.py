# 封装：就是把属性或方法装起来

# 广义：就是把属性或方法装起来，外面不能直接调用了，要通过类的名字来调用
# 狭义：把属性和方法藏起来了，外面不能掉用了，只能在内部偷偷调用

# 私有的实例变量/私有的对象属性
# class User:
#     def __init__(self,name, passwd):
#         self.usr = name
#         self.__pwd = passwd    # 私有的实例变量/私有的对象属性
#     # def get_pwd(self):   # 表示的是用户不能改只能看 私有 + 某个get方法实现的
#     #     return self.__pwd
#     # def change_pwd(self):   # 表示用户必须调用我们自定义的修改方式来进行变量的修改 私用 + change方法实现
#     #     pass

# alex = User('alex', 'sbsb')
# print(alex.pwd)
# print(alex.get_pwd())

# 给一个名字前面加上了双下划线的时候,这个名字就变成了一个私有的
# 所有的私有的内容或者名字都不能在类的外部调用,只能在类的内部使用了

# 私有的静态变量
# class User:
#     __Country = 'China'  # 私有的静态变量
#     def func(self):
#         print(User.__Country)  # 在类的内部可以调用
# print(User.Country)  # 报错 在类的外部不能调用
# User().func()

# 私有方法
import hashlib
class User:
    def __init__(self, name, passwd):
        self.name = name
        self.__passwd = passwd
    def __get_md5(self):
        md5 = hashlib.md5()
        md5.update(self.__passwd.encode('utf-8'))
        return md5.hexdigest()
    def getpwd(self):
        return self.__get_md5()

# alex = User('alex', 'sbsb')
# # alex.__get_md5()    # 错误
# ret = alex.getpwd()
# print(ret)

# 所有的私有化都是为了让用户不在外部调用类中的某个名字
# 在py中一般比较少用py私有方法，也就是一般情况下不加__名字
# 如果完成私有化 那么这个类的封装度就更高了 封装度越高各种属性和方法的安全性也越高 但是代码越复杂

# 加了双下划线的方法为啥不能调用了
# class User:
#     __Country = 'China'    # '_User__Country': 'China'
#     role = '法师'    #  'role': '法师'
#     def func(self):    #  # 在类的内部使用的时候,自动的把当前这句话所在的类的名字拼在私有变量前完成变形
#         print(self.__Country)
# print(User.__dict__)
# # print(User._User__Country)
# ret = User()
# print(ret.func())

# 私有的内容能不能被子类使用呢? 不能
# class Foo(object):
#     def __init__(self):
#         self.func()
#     def func(self):
#         print('in Foo')
# class Son(Foo):
#     def func(self):
#         print('in Son')
# Son()
# class Foo(object):
#     def __init__(self):
#         self.__func()
#     def __func(self):
#         print('in Foo')
# class Son(Foo):
#     def __func(self):
#         print('in Son')
# Son()
# class Foo(object):
#     def __func(self):
#         print('in Foo')
# class Son(Foo):
#     def __init__(self):
#         self.__func()
# Son()
# 在其它语言中的数据的级别都有那些？在py中有哪些？
# public 共有的 类内类外都能用，父类子类都能用       python支持
# private 保护的 类内能用，父类子类都能用 类外不能用  python不支持
# private 私有的 本类的类内部能用,其他地方都不能用    python支持


































