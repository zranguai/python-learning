"""
作业：用代码模拟博客园系统。

项目分析：
一．首先程序启动，页面显示下面内容供用户选择：

1.请登录
2.请注册
3.进入文章页面
4.进入评论页面
5.进入日记页面
6.进入收藏页面
7.注销账号
8.退出整个程序

二．必须实现的功能：

1.注册功能要求：
a.用户名、密码要记录在文件中。
b.用户名要求：只能含有字母或者数字不能含有特殊字符并且确保用户名唯一。
c.密码要求：长度要在6~14个字符之间。
d.超过三次登录还未成功，则退出整个程序。

2.登录功能要求：
a.用户输入用户名、密码进行登录验证。
b.登录成功之后，才可以访问3~7选项，如果没有登录或者登录不成功时访问3~7选项，不允许访问，让其先登录。（装饰器）

3.进入文章页面要求：
a.提示欢迎xx进入文章页面。
b.此时用户可以选择：直接写入内容，还是导入md文件。
①如果选择直接写内容：让学生直接写文件名|文件内容......最后创建一个文章。

②如果选择导入md文件：让用户输入已经准备好的md文件的文件路径（相对路径即可：比如函数的进阶.md），然后将此md文件的全部内容写入文章（函数的进阶.text）中。

4.进入评论页面要求：
提示欢迎xx进入评论页面。

5.进入日记页面要求：
提示欢迎xx进入日记页面。
6.进入收藏页面要求：
提示欢迎xx进入收藏页面。

7.注销账号要求：
不是退出整个程序，而是将已经登录的状态变成未登录状态（访问3~7选项时需要重新登录）。

8.退出整个程序要求：
就是结束整个程序。
"""
status_dict = {
    'username': None,
    'status': False
}
register_path = r'D:\老男孩python22期代码及笔记\day17\register'
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
    with open(register_path, mode='a', encoding='utf-8') as f1:
        username = input('请输入用户名')
        password = input('请输入密码')
        while 1:
            if len(password) <= 6 or len(password) > 14:
                password = input('请重新输入密码')
            else:
                print('你的密码长度在6到14之间，输入正确')
                break
        f1.write(f'{username}|{password}\n')
# 装饰器
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
    print('欢迎进入文章页面')
@auth
def comment():
    print('欢迎进入评论页面')
@auth
def dariy():
    print('欢迎进入日记页面')
@auth
def collections():
    print('欢迎进入收藏页面')
def login_out():
    print('注销账号')
    status_dict['status'] = False
import os
def _quit():
    print('退出程序')
    os._exit()
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
