# 装饰器的应用：登入认证
# 周末作业：模拟博客园登入的作业。装饰器的认证功能


def login():
    print('请完成登入功能')

def register():
    print('请完成注册功能')

status_dict = {
    'username': None,
    'status': False
}
# 装饰器：你的装饰器完成：访问被装饰函数之前，写一个三次登入认证的功能
# 登入成功：让其访问被装饰的函数，登入没有成功，不让访问
def auth(f):
    def inner(*args, **kwargs):
        """访问函数之前操作"""
        if status_dict['status']:
            ret = f(*args, **kwargs)
            """访问函数之后操作"""
            return ret
        else:
            username = input('请输入用户名')
            password = input('请输入密码')
            if username == 'taibai' and password == '123':
                status_dict['username'] = username
                status_dict['status'] = True
                ret = f(*args, **kwargs)
                return ret
            else:
                print('登入失败')

    return inner

@auth    # article = auth(article)
def article():
    print('欢迎访问文章页面')

@auth
def comment():
    print('欢迎访问评论页面')

@auth
def dariy():
    print('欢迎访问日记页面')

article()
comment()
dariy()
