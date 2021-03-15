# __new__
class A:
    def __new__(cls, *args, **kwargs):    # 构造方法
       o = super().__new__(cls)    # 开空间
       print('执行了new', o)
       return o
    def __init__(self):
        print('执行了init', self)

# A()

# 实例化的时候
# 先创建一块对象的空间,有一个指针能指向类 --> __new__
# 调用init --> __init__


# 记忆
# 设计模式----单例模式（平时不用，只有在面试时会用到）
# 一个类  从头到尾 只会创建一次self空间(实例化只会开一个空间)
class Baby:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self,cloth,pants):
        self.cloth = cloth
        self.pants = pants
b1 = Baby('红毛衣','绿皮裤')
print(b1.cloth)
b2 = Baby('白衬衫','黑豹纹')
print(b1)
print(b2)
print(b1.cloth)
print(b2.cloth)




# from 单例 import baby
# print(baby)
# print(baby)
# print(baby)














































