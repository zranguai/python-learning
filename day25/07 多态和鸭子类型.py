# 多态
# def add(int a,int b):
#     return a+b
#
# print(add(1,'asuhjdhDgl'))

# class Payment:pass    # java中必须搞一个父类
# class WeChat(Payment):
#     def __init__(self,name):
#         self.name = name
#     def pay(self,money):
#         dic = {'username':self.name,'money':money}
#         # 想办法调用微信支付 url连接 把dic传过去
#         print('%s通过微信支付%s钱成功'%(self.name,money))
#
# class Apple(Payment):
#     def __init__(self,name):
#         self.name = name
#     def pay(self,money):
#         dic = {'name': self.name, 'number': money}
#         # 想办法调用苹果支付 url连接 把dic传过去
#         print('%s通过苹果支付%s钱成功' % (self.name, money))


#JAVA
# def pay(Payment a, int b):
# #     a.pay(b)
# # obj = Apple('alex')
# # pay(obj,400)
# # obj = WeChat('alex')
# # pay(obj,400)

# python中处处是多态（因为他没有类型限制）

# 背
# 一个类型表现出来的多种状态（通过继承来实现）
# 支付 表现出的 微信支付和苹果支付这两种状态
# 在java情况下: 一个参数必须制定类型
# 所以如果想让两个类型的对象都可以传,那么必须让这两个类继承自一个父类,在制定类型的时候使用父类来指定


# 鸭子类型
# class list:
#     def __init__(self,*args):
#         self.l = [1,2,3]
#     def __len__(self):
#         n = 0
#         for i in self.l:
#             n+= 1
#         return n
# l = [1,2,3]
# l.append(4)
# def len(obj):
#     return obj.__len__()

# 所有实现了__len__方法的类,在调用len函数的时候,obj都说是鸭子类型
#
# 迭代器协议 __iter__ __next__ 是迭代器

# class lentype:pass
#
# class list(lentype):pass
# class dict(lentype):pass
# class set(lentype):pass
# class tuple(lentype):pass
# class str(lentype):pass
#
# def len(lentype obj):
#     pass
#
# len(list)
# len(dict)
# len(set)
# len(tuple)
# len(str)

# class list:
#     def __len__(self):pass
# class dict:
#     def __len__(self): pass
# class set:
#     def __len__(self): pass
# class tuple:
#     def __len__(self): pass
# class str:
#     def __len__(self): pass
#
# def len(鸭子类型看起来有没有实现一个__len__ obj):
#     return obj.__len__()



# super是重要的（明天写）












