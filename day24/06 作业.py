# day21
# 1.完成下列功能:
#
# 1.创建一个人类Person,再类中创建3个静态变量(静态字段) animal = '高级动物' soul = '有灵魂' language = '语言'
# 2.在类中定义三个方法,吃饭,睡觉,工作.
# 3.在此类中的__init__方法中,给对象封装5个属性:国家,姓名,性别,年龄, 身高.
# 4.实例化四个人类对象: 第一个人类对象p1属性为:中国,alex,未知,42,175. 第二个人类对象p2属性为:美国,武大,男,35,160. 第三个人类对象p3属性为:你自己定义. 第四个人类对象p4属性为:p1的国籍,p2的名字,p3的性别,p2的年龄,p3 的身高.
# 5.通过p1对象执行吃饭方法,方法里面打印:alex在吃饭.
# 6.通过p2对象执行吃饭方法,方法里面打印:武大在吃饭.
# 7.通过p3对象执行吃饭方法,方法里面打印:(p3对象自己的名字)在吃饭.
# 8.通过p1对象找到Person的静态变量 animal
# 9.通过p2对象找到Person的静态变量 soul
# 10.通过p3对象找到Person的静态变量 language
# class Person:
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#     def __init__(self, nation, name, sex, age, height):
#         self.natioon = nation
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.height = height
#     def eat(self):
#         print(f'{self.name}在吃饭')
#     def sleep(self):
#         pass
#     def work(self):
#         pass
#
#
# p1 = Person('中国', 'alex', '未知', 42, 175)
# p2 = Person('美国','武大','男',35,160)
# p3 = Person('澳大利亚', 'heha', '女', 32, 178)
# p4 = Person(p1.natioon, p2.name, p3.sex, p2.age, p3.height)
# p1.eat()
# p2.eat()
# p3.eat()
# print(p1.animal)
# print(p2.soul)
# print(p3.language)


# 2.通过自己创建类,实例化对象 在终端输出如下信息
# 小明，10岁，男，上山去砍柴
# 小明，10岁，男，开车去东北
# 小明，10岁，男，最爱大保健
# 老李，90岁，男，上山去砍柴
# 老李，90岁，男，开车去东北
# 老李，90岁，男，最爱大保健
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def info(self):
#         info = ['上山去砍柴', '开车去东北', '最爱大保健']
#         for i in info:
#             print(f'{self.name}, {self.age}岁, {self.sex},{i}')
#
# h1 = Human('小明', 10, '男')
# h1.info()
# h2 = Human('老李', 90, '男')
# h2.info()


# 3.设计一个汽车类。
#
# 要求：
#
# 汽车的公共属性为：动力驱动，具有四个或以上车轮，主要用途载运人员或货物。 汽车的功能：run,transfer.
#
# 具体的汽车的不同属性：颜色，车牌，类型（越野，轿车，货车等）。
# class Class:
#     power = '动力驱动'
#     wheel = '具有四个或以上车轮'
#     usage = '载运人员或货物'
#     def __init__(self, color, number, type):
#         self.color = color
#         self.number = number
#         self.type = type
#     def run(self):
#         print('开')
#     def transfer(self):
#         print('转换')
#

# 4.模拟英雄联盟写一个游戏人物的类（升级题）. 要求:
#
# 1.创建一个 Game_role的类.
#
# 2.构造方法中给对象封装name,ad(攻击力),hp(血量).三个属性.
#
# 3。创建一个attack方法,此方法是实例化两个对象,互相攻击的功能:
# 例: 实例化一个对象 盖伦,ad为10, hp为100
# 实例化另个一个对象 剑豪 ad为20, hp为80
# 盖伦通过attack方法攻击剑豪,此方法要完成 '谁攻击谁,谁掉了多少血, 还剩多少血'的提示功能.

# class Game_role:
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attact(self, name):
#         name.hp -= self.ad
#         print(f'{self.name}攻击{name.name},{name.name}掉了{self.ad}血, 还剩{name.hp}血')
#         if name.hp < 0:
#             print(f'{name.name}死了')
#
# p1 = Game_role('盖伦', 10, 100)
# p2 = Game_role('剑豪', 20, 80)
#
# p1.attact(p2)
# p1.attact(p2)
# p1.attact(p2)
# p1.attact(p2)
# p1.attact(p2)
# p2.attact(p1)


# day22
# 1. 暴力摩托程序（完成下列需求）：
#
#    1. 创建三个游戏人物，分别是：
#
#       ​	苍井井，女，18，攻击力ad为20，血量200
#
#       ​	东尼木木，男，20，攻击力ad为30，血量150
#
#       ​	波多多，女，19，攻击力ad为50，血量80
#
#    2. 创建三个游戏武器，分别是：
#
#       ​   平底锅，ad为20
#
#       ​	斧子，ad为50
#
#       ​	双节棍，ad为65
#
#    3. 创建三个游戏摩托车，分别是：
#
# ​				小踏板，速度60迈
#
# ​				雅马哈，速度80迈
#
# ​				宝马，速度120迈。
#
# ​	完成下列需求（利用武器打人掉的血量为武器的ad + 人的ad）：
#
# ​	（1）苍井井骑着小踏板开着60迈的车行驶在赛道上。
#
# ​	（2）东尼木木骑着宝马开着120迈的车行驶在赛道上。
#
# ​	（3）波多多骑着雅马哈开着80迈的车行驶在赛道上。
#
# ​	（4）苍井井赤手空拳打了波多多20滴血，波多多还剩xx血。
#
# ​	（5）东尼木木赤手空拳打了波多多30滴血，波多多还剩xx血。
#
# ​	（6）波多多利用平底锅打了苍井井一平底锅，苍井井还剩xx血。
#
# ​	（7）波多多利用斧子打了东尼木木一斧子，东尼木木还剩xx血。
#
# ​	（8）苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。（选做）
#
# ​	（9）波多多骑着小踏板打了骑着雅马哈的东尼木木一斧子，东尼木木哭了，还剩xx血。（选做）

# class Game_characters:
#     def __init__(self, name, sex, age, ad, hp):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.ad = ad
#         self.hp = hp
#     def start_drive(self, obj):
#         self.car = obj
#     def weapon_attact(self, obj):
#         self.weapon = obj
#     def attact(self, obj):
#         obj.hp -= self.ad
#         print(f'{self.name}赤手空拳打了{obj.name}{self.ad}滴血，{obj.name}还剩{obj.hp}血')
# # 苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。
# class Weapon:
#     def __init__(self, name, ad):
#         self.name = name
#         self.ad = ad
#     def weapon_attact(self, obj1, obj2):
#         obj2.hp -= (obj1.ad + self.ad)
#         print(f'{obj1.name}利用{self.name}打了{obj2.name}一{self.name}，{obj2.name}还剩{obj2.hp}血')
#
# class Motor_cycle:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#     def drive(self, obj):
#         print(f'{obj.name}骑着{self.name}开着{self.speed}迈的车行驶在赛道上')
#     def drive_attact(self, obj1, obj2):
#         obj2.hp = obj2.hp - obj1.ad - obj1.weapon.ad
#         print(f'{obj1.name}骑着{obj1.car.name}打了骑着{obj2.car.name}的{obj2.name}一{obj1.weapon.name}，{obj2.name}哭了，还剩{obj2.hp}血。')
#
# # 苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。
# G1 = Game_characters('苍井井', '女', 18, 20, 200)
# G2 = Game_characters('东尼木木', '男', 20, 30, 150)
# G3 = Game_characters('波多多', '女', 19, 50, 80)
#
# W1 = Weapon('平底锅', 20)
# W2 = Weapon('斧子', 50)
# W3 = Weapon('双截棍', 65)
#
# M1 = Motor_cycle('小踏板', 60)
# M2 = Motor_cycle('雅马哈', 80)
# M3 = Motor_cycle('宝马', 120)
#
# M1.drive(G1)
# M3.drive(G2)
# M2.drive(G3)
# G1.attact(G3)
# G2.attact(G3)
# W1.weapon_attact(G3, G1)
# W2.weapon_attact(G3, G2)
#
# G1.start_drive(M3)  # 把对象传过去
# G2.start_drive(M1)
# G1.weapon_attact(W3)
# M3.drive_attact(G1, G2)


# 4. 定义一个学校类，一个老师类。
#
#    - 学校类要求：
#
#      - 学校类封装学校名称，学校地址，以及相关老师（以列表形式存放老师对象）的  属性。
#        - name: 学校名称。
#        - address: 具体地址。
#        - teacher_list: []。
#
#      - 学校类设置添加老师对象的  方法。
#
#    - 老师类封装姓名，教授学科，以及所属学校的具体对象。
#
#      - name: 老师名。
#      - course: 学科。
#      - school: 具体学校对象。
#
#    - 实例化2个校区：
#
#      - 北京校区，美丽的沙河；
#      - 深圳校区，南山区。
#
#    - 实例化6个老师：
#
#      - 太白，Python, 北京校区对象。
#      - 吴超，linux, 北京校区对象。
#      - 宝元，python, 北京校区对象。
#      - 苑昊，python, 深圳校区对象。
#      - 小虎，linux, 深圳校区对象。
#      - 小王，Python，深圳校区对象。
#
#    - 完成以下具体需求：
#
#      1. 获取太白所属学校名称。
#      2. 获取太白所属学校的学校地址。
#
#      3. 将所有属于北京校区的所有老师名展示出来，并添加到一个列表中。
#
#      4. 将所有属于深圳校区的所有老师以及所负责的学科展示出来。
#
#      5. 将两个校区的负责Python学科的所有老师对象添加到一个列表中。
#
#      6. 将两个校区的负责linux学科的所有老师对象添加到一个列表中并循环展示出来。
#      7. 将北京校区这个对象利用pickle写入文件中，然后读取出来，并展示出所属于北京校区的老师姓名。
class School:
    def __init__(self, name, address, teacher_list):
        self.name = name
        self.address = address
        self.teacher_list = teacher_list
    def append_teacher(self, obj):
        self.teacher_list.append(obj)

class Teacher(School):
    def __init__(self, name, course, school):
        self.name = name
        self.course = course
        self.school = school
s1 = School('北京校区', '美丽的沙河', [])
s2 = School('深圳校区', '南山区', [])

t1 = Teacher('太白', 'Python', s1)
t2 = Teacher('吴超', 'linux', s1)
t3 = Teacher('宝元', 'Python', s1)
t4 = Teacher('苑昊', 'Python', s2)
t5 = Teacher('小虎', 'linux', s2)
t6 = Teacher('小王', 'Python', s2)

s1.append_teacher(t1)
s1.append_teacher(t2)
s1.append_teacher(t3)
s2.append_teacher(t4)
s2.append_teacher(t5)
s2.append_teacher(t6)
# 1.
# print(t1.school.name)
# print(t1.school.address)
# 2
# lst = []
# for i in s1.teacher_list:
#     print(i.name)
#     lst.append(i.name)
# print(lst)
#
# for i in s2.teacher_list:
#     print(i.name)
#     print(i.course)

# lst1 = []
# for i in s1.teacher_list:
#     if i.course == 'Python':
#         lst1.append(i)
# for i in s2.teacher_list:
#     if i.course == 'Python':
#         lst1.append(i)
#
# print(lst1)
#
# lst2 = []
# for i in s1.teacher_list + s2.teacher_list:
#     if i.course == 'linux':
#         print(i.name)
#         lst2.append(i)

# 将北京校区这个对象利用pickle写入文件中，然后读取出来，并展示出所属于北京校区的老师姓名
# import pickle
# # with open('pickkk', mode='wb') as f:
# #     pickle.dump(s2, f)
#
# with open('pickkk', mode='rb') as f1:
#     ret = pickle.load(f1)
#     for i in ret.teacher_list:
#         print(i.name)
#
#
# day23作业
















