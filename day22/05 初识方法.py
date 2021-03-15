class Person:    # 类名
    def __init__(self,name,sex,job,level,hp,weapon,ad):
        # 必须叫__init__这个名字,不能改变的,所有的在一个具体的人物出现之后拥有的属性,都写在这里
        # self 是具体的对象
        self.name = name    # 对象的属性/实例变量
        self.sex = sex
        self.job = job
        self.level = level
        self.hp = hp
        self.weapon = weapon
        self.ad = ad
    def cuo(self, dog):    # 方法，有一个必须传的参数self
        # print('whaha', self)
        # print(self.name)
        dog.hp -= self.ad
        print(f"{self.name}给{dog.name}搓澡{dog.name}掉了{self.ad}点血")
class Dog:
    def __init__(self, name, kind, hp, ad):
        self.name = name
        self.kind = kind
        self.hp = hp
        self.ad = ad
    def tian(self, person):
        # print(self.__dict__)
        person.hp -= self.ad
        print(f"{self.name}舔了{person.name}，{person.name}掉了{self.ad}点血")

alex = Person('alex', '不详', '搓澡工', 0,250,'搓澡巾',1)    # 对象/实例=类名()--->实例化过程
# print('alex', alex)
# alex.cuo()

xiaobai = Dog('xiaobai', '土狗', 5000, 10)
# xiaobai.tian()
# alex.cuo(xiaobai)
xiaobai.tian(alex)









