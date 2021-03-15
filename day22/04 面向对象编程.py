# 想来定义一类模子，用来描述一类事物
# 具有相同的属性和功能

# 类里面一个tab键类会执行
class Person:    # 类名
    def __init__(self,name,sex,job,level,hp,weapon,ad):
        # 必须叫__init__这个名字,不能改变的,所有的在一个具体的人物出现之后拥有的属性,都写在这里
        # self 是具体的对象
        self.name = name
        self.sex = sex
        self.job = job
        self.level = level
        self.hp = hp
        self.weapon = weapon
        self.ad = ad
        # print(self, self.__dict__)
alex = Person('alex', '不详', '搓澡工', 0,250,'搓澡巾',1)    # alex 就是对象  alex = Person()的过程 是通过类获取一个对象的过程 --->实例化
# print(alex, alex.__dict__)    # __dict__查看类中的属性和值
print(alex.name)      # 属性的查看  等同于print(alex.__dict__['name'])
alex.name = 'alexsb'    # 属性的修改
alex.money = 10000      # 属性的增加
# print(alex.__dict__)
del alex.money          # 属性的删除
# print(alex.__dict__)


wusir = Person('wusir','male','法师',0,500,'打狗棍',1000)
# 类名() 会自动调用类中的__init__()方法

# 类和对象之间的关系?
# 类 是一个大范围 是一个模子 他约束了事物有哪些属性，但是不能约束具体的值
# 对象 是一个具体的内容 是模子的产物 它遵循了类的约束 同时给属性赋上具体的值

# Person是一个类  alex.wusir都是这个类的对象
# 类有一个空间,存储的是定义在class中的所有名字
# 每一个对象又拥有自己的空间,通过对象名.__dict__就可以查看这个对象的属性和值


# 实例化所经历的步骤：
# 1.类名()之后的第一件事情：开辟一块内存空间（重要）
# 2.调用__init__把空间的内存地址作为self参数传递到函数内部
# 3.所有的这一个对象需要使用的属性都需要和self关联起来
# 4.执行完__init__中的逻辑后，self变量会自动的被返回到调用处（发生实例化的地方）


# 补充：修改对象/列表/字典中的某个值，或者是对象的某一个属性，都不会影响这个对象/列表/字典所在的内存空间


# 练习题1：
# 实现Dog类 实现狗的名字 品种，血量，攻击力  都可以通过实例化定制
class Dog:
    def __init__(self, name, kind, hp, ad):
        self.name = name
        self.kind = kind
        self.hp = hp
        self.ad = ad

xiaobai = Dog('xiaobai', '土狗', 5000, 10)
print(xiaobai.name) # 查
xiaobai.hp = 4000   # 改
print(xiaobai.hp)
xiaobai.sex = 'mail' # 增加
print(xiaobai.sex)
del xiaobai.ad
print(xiaobai.__dict__)

# 练习题2
# 定义一个圆形类，半径是这个圆形的属性，实例化一个半径为5的圆形，一个半径为10的圆形
# 完成方法：计算圆的面积，计算园的周长
# 定义一个用户类，用户名和密码是这个类的属性，实例化两个用户，分别有不同的用户名和密码
# 完成方法：
# 登入成功后才创建用户对象
# 设计一个方法 修改密码
# （之前密码，修改后密码）



# 继续完成人狗大战
# 你是人
# 狗是一个npc
# 你一个回合，狗一个回合
# 狗掉的血是一个波动值
# 闪避概率

# 继续完成计算器






















