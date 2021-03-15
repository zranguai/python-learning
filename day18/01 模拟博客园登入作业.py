
status_dict = {
    'username': None,
    'status': False
}
register_path = r'/day18/blog/db/register'

def get_user_pwd():
    user_dict = {}
    with open(register_path, encoding='utf-8') as f:
        for line in f:
            line_list = line.strip().split('|')
            user_dict[line_list[0].strip()] = line_list[1].strip()
            print(user_dict)
        return user_dict

def login():
    u_dict = get_user_pwd()
    count = 1
    while count < 4:
        username = input('请输入用户名').strip()
        passworrd = input('请输入密码').strip()
        if username in u_dict and passworrd == u_dict[username]:
            print('登入成功')
            status_dict['username'] = username
            status_dict['status'] = True
            return True
        else:
            print('用户名或密码错误...请重新登入')
        count += 1


def register():
    print('请完成注册功能')

# 装饰器：你的装饰器完成：访问被装饰函数之前，写一个三次登入认证的功能
# 登入成功：让其访问被装饰的函数，登入没有成功，不让访问
def auth(f):
    def inner(*args, **kwargs):
        if status_dict['status'] == True:
            """访问函数之前操作"""
            ret = f(*args, **kwargs)
            """访问函数之后操作"""
            return ret
        else:
            if login():
                ret = f(*args, **kwargs)
                return ret
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

@auth
def collections():
    print('欢迎访问收藏页面')
def login_out():
    pass
def _quit():
    pass

dic = {
    1: login,
    2: register,
    3: article,
    4: comment,
    5: dariy,
    6: collections,
    7: login_out,
    8: _quit,
}
def run():
    while True:
        print("""
        1.请登录
        2.请注册
        3.进入文章页面
        4.进入评论页面
        5.进入日记页面
        6.进入收藏页面
        7.注销账号
        8.退出整个程序
        """)
        num = input('请输入选项').strip()
        num = int(num)
        dic[num]()

run()
