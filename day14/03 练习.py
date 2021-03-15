# 01装饰器的初识
# 装饰器：给他加个延时
# import time
# def timmer(f):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         r = f(*args, **kwargs)
#         end_time = time.time()
#         print(end_time - start_time)
#         return r
#     return inner
#
# @timmer    # index = timmer(index)
# def index(name, age):
#     time.sleep(0.5)
#     print(f'欢迎{age}岁的{name}来到首页')
#
# @timmer
# def comment(name):
#     time.sleep(0.4)
#     print(f'欢迎{name}来到评论页')
#
# index('小明', 20)
# comment('小花')

# 02装饰器的应用
status_dict = {
    'name': None,
    'status': False
}
def auth(f):
    def inner(*args, **kwargs):
        if status_dict['status'] == True:
            print('登入成功')
            r = f(*args, **kwargs)
            return r
        else:
            name = input('请输入名字')
            password = input('请输入密码')
            if name == 'haha' and password == '123':
                status_dict['status'] = True
                status_dict['name'] = 'haha'
                r = f(*args, **kwargs)
                return r
            else:
                print('登入失败')
    return inner

@auth    # article = auth(article)
def article():
    print('欢迎登入文章页面')

@auth
def comment():
    print('欢迎登入评论页面')

@auth
def dariy():
    print('欢迎登入日记页面')

article()
comment()
dariy()
