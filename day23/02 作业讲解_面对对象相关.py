# 定义一个用户类，用户名和密码是这个类的属性，实例化两个用户，分别有不同的用户名和密码
# 完成方法：
# 登入成功后才创建用户对象
# 设计一个方法 修改密码
# （之前密码，修改后密码）
# ******重做****把原来密码以及要修改的密码放进文件中
def login(username, password):
    if username == 'xiaoming' and password == '123':
        return True
    else:
        return False


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def change_pwd(self, newpwd):
        self.password = newpwd


username = input('username')
password = input('password')
if login(username, password):
    xiaoming = User('小明', 123)
    xiaohong = User('小红', 456)
    print(xiaohong.username)
    print(xiaohong.password)
    xiaohong.change_pwd(789)
    print(xiaohong.password)
else:
    print('输入错误')