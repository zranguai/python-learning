
# class User:
#     def __init__(self, name, pwd):
#         self.name = name
#         self.pwd = pwd
#
# class Account:
#     def __init__(self):
#         # 用户列表，数据格式：[user对象，user对象，user对象]
#         self.user_list = []
#
#     def login(self):
#         # 登录
#         # 登录 输入用户名密码
#         # 和self.user_list作比对
#         username = input('用户名 :')
#         password = input('密  码 :')
#         for user in self.user_list:
#             if username == user.name and password == user.pwd:
#                 print('登录成功')
#                 break
#         else:
#             print('登录失败')
#
#     def register(self):
#         # 注册
#         # 注册成功了之后,user对象存在user_list里
#         username = input('用户名 :')
#         password = input('密  码 :')
#         password2 = input('密码确认 :')
#         if password == password2:
#             user = User(username,password)
#             self.user_list.append(user)
#             print('注册成功')
#         else:
#             print('注册失败,您两次输入的密码不一致')
#
#     def run(self):
#         opt_lst= ['登录','注册']
#         while True:
#             for index,item in enumerate(opt_lst,1):
#                 print(index,item)
#             num = input('请输入您需要的操作序号 :').strip()
#             if num == '1':
#                 self.login()
#             elif num == '2':
#                 self.register()
#             elif num.upper() == 'Q':
#                 break
#
# if __name__ == '__main__':
#     obj = Account()
#     obj.run()

####################作业#################################
# 注册之后,重启所有的用户丢失
# 一次执行的注册行为,在之后所有执行中都能够正常登录
# 两个登录程序和面向对象的内容整理在一起,两个都要明白,都要记住
###################作业##################################
# 写一个自定义模块,里面有你自己实现的mypickle和myjson,我只需要给你传递一个参数 'pickle'还是'json'

# class Foo(object):
#     n1 = '武沛齐'
#     def __init__(self,name):
#         self.n2 = name
# obj = Foo('太白')
# print(obj.n1)
# print(obj.n2)
#
# print(Foo.n1)
# print(Foo.n2)