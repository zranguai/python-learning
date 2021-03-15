# 学生选课系统：
# https://www.cnblogs.com/Eva-J/articles/9235899.html
# 1.把类创建出来
# 2.把属性写上
# 3.把函数名写上
# 接下来要完善的两个地方
# 用户的登入---自动识别出身份
# 思考：登入之后从那个功能写起


class Course(object):

    def __init__(self, name, price, cycle):
        self.name = name
        self.price = price
        self.cycle = cycle


class Student(object):

    def __init__(self, name):
        self.name = name

    def show_courses(self):     # 查看可选课程
        pass

    def choose_course(self):    # 选择课程
        pass

    def show_selected(self):       # 查看所选课程
        pass

    def exit(self):
        pass


class Manager(object):

    def __init__(self, name):
        self.name = name

    def create_course(self):
        pass

    def create_student(self):
        pass

    def show_courses(self):
        pass

    def show_students(self):
        pass

    def show_stu_course(self):
        pass

    def exit(self):
        pass


# 用户输入用户名 密码 判断用户是否合法和身份是啥？







# 管理员登入 管理员：admin 123
# 创建
    # 学生（让用户输入学生信息，然后实例化，然后写到学生文件中）[pickle]
    # 课程（让用户输入课程信息，然后实例化，然后写到课程文件里）

# 学生可以选多门口 怎么存
# 学生只要选课--文件修改（麻烦）


# 用上反射就简单
# 能不能 不管是学生登入 还是管理员登入 不用if/else---进阶

# form 模块 import 一个类
# import sys
# getattr(sys.modules[__name__],'名字')反射本模块中的内容






