# raise KeyError('提示信息')    # 主动抛异常
# raise NotImplementedError('没有按照要求实现函数')
# 抽象类
# 是一个开发的规范 约束他的子类必须实现一些与他同名的方法

# 支付程序
    # 微信支付 url连接,告诉你参数什么格式
        # {'username':'用户名','money':200}
    # 支付宝支付 url连接,告诉你参数什么格式
        # {'uname':'用户名','price':200}
    # 苹果支付

# 方式1：手动抛出异常 一般用这个
# class Payment:     # 抽象类
#     def pay(self,money):
#         '''只要你见到了项目中有这种类,你要知道你的子类中必须实现和pay同名的方法'''
#         raise NotImplementedError('请在子类中重写同名pay方法')
#
# class Alipay(Payment):
#     def __init__(self,name):
#         self.name = name
#     def pay(self,money):
#         dic = {'uname':self.name,'price':money}
#         # 想办法调用支付宝支付 url连接 把dic传过去
#         print('%s通过支付宝支付%s钱成功'%(self.name,money))
#
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
#     def fuqian(self,money):
#         dic = {'name': self.name, 'number': money}
#         # 想办法调用苹果支付 url连接 把dic传过去
#         print('%s通过苹果支付%s钱成功' % (self.name, money))
#
# aw = WeChat('alex')
# aw.pay(400)
# aa = Alipay('alex')
# aa.pay(400)

# # 归一化设计
def pay(name,price,kind):
    if kind == 'Wechat':
        obj = WeChat(name)
    elif kind == 'Alipay':
        obj = Alipay(name)
    elif kind == 'Apple':
        obj = Apple(name)
    obj.pay(price)

pay('alex',400,'Wechat')
pay('alex',400,'Alipay')
pay('alex',400,'Apple')
#
# appa = Apple('alex')
# appa.fuqian(500)
# 方式1缺点，实例化时不能报错，只有调用方法时才会报错



# 方式2：利用abc模块
# 实现抽象类的另一种方式,约束力强,依赖abc模块
from abc import ABCMeta, abstractmethod
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):    # 该方法一定要实现，且同名
        '''只要你见到了项目中有这种类,你要知道你的子类中必须实现和pay同名的方法'''
        raise NotImplementedError('请在子类中重写同名pay方法')

class Alipay(Payment):
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        dic = {'uname':self.name,'price':money}
        # 想办法调用支付宝支付 url连接 把dic传过去
        print('%s通过支付宝支付%s钱成功'%(self.name,money))

class WeChat(Payment):
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        dic = {'username':self.name,'money':money}
        # 想办法调用微信支付 url连接 把dic传过去
        print('%s通过微信支付%s钱成功'%(self.name,money))

WeChat('alex')







