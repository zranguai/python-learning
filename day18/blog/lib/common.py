# 装饰器：你的装饰器完成：访问被装饰函数之前，写一个三次登入认证的功能
# 登入成功：让其访问被装饰的函数，登入没有成功，不让访问
from core import src
def auth(f):
    def inner(*args, **kwargs):
        if src.status_dict['status'] == True:
            """访问函数之前操作"""
            ret = f(*args, **kwargs)
            """访问函数之后操作"""
            return ret
        else:
            if src.login():
                ret = f(*args, **kwargs)
                return ret
    return inner
