# 组合：一个类的对象是例外一个类对象的属性---->对象变成了一个属性

# 学生类
# 班级信息：班级名字 开班时间 当前讲师
class Student:
    def __init__(self, name, age, sex, calc):
        self.name = name
        self.age = age
        self.sex = sex
        self.calc = calc

class Clas:
    def __init__(self, cname, begin_time, teacher):
        self.cname = cname
        self.begin_time = begin_time
        self.teacher = teacher

# py22 = Clas('python23', '2019-5-28', 'eva-j')
# py23 = Clas('python22', '2019-4-26', 'eva-j')
# 大壮 = Student('大壮',18, 'male', py22)
# 雪飞 = Student('雪飞',25, 'female', py23)
# print(大壮.calc, py22)    # 大壮.calc等同于py22
# print(py22.begin_time)
# print(大壮.calc.begin_time)

# 需求：查看大壮的班级的开办日期是多少

# 练习客户端合法性：
# 班级类
# 包含了一个属性-课程
# 课程
# 课程名称
# 周期
# 价格

# 创建两个班级：linux57
# 创建两个班级：python22

# 要求：
# 查看linux57期的班级所学课程的价格
# 查看python22期的班级所学课程的周期
class Course:    # 课程类
    def __init__(self,k_name, k_cycle, k_price):
        self.k_name = k_name
        self.k_cycle = k_cycle
        self.k_price = k_price

class Calc:    # 班级类
    def __init__(self, cname, begin_time, teacher, course):
        self.cname = cname
        self.begin_time = begin_time
        self.teacher = teacher
        self.course = course

course = Course('正则表达式', '54周', 21000)    # 课程对象
linux57 = Calc('linux57', '2019-5-28', 'evaj', course)    # 班级对象
python22 = Calc('python22', '2019-4-26', '太白', course)   # 班级对象

print(linux57.course.k_price)
print(python22.course.k_cycle)










