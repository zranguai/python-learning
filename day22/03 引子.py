# 游戏公司
    # 人狗大战
# 人 :
    # 名字 性别 职业 等级 血条 武器 攻击力
    # 技能 : 搓澡
# 狗 :
    # 名字 品种 血条 攻击力
    # 技能 : 舔

# alex = {
#     'name': 'alex',
#     'sex': '不详',
#     'job': '搓澡工',
#     'level': 0,
#     'hp' : 250,
#     'weapon':'搓澡巾',
#     'ad' : 1
# }
# 小白 = {
#     'name':'小白',
#     'kind':'泰迪',
#     'hp':5000,
#     'ad':249
# }

# 1.你怎么保证所有的玩家初始化的时候都拥有相同的属性
# 2.每来一个新的玩家,我们都自己手动的创建一个字典,然后向字典中填值
# 3.人物和狗的技能如何去写

def Person(name,sex,job,hp,weapon,ad,level=0):  # 人模子
    def cuo(dog):
        dog['hp'] -= dic['ad']
        print(f"{dic['name']}攻击了{dog['name']},{dog['name']}掉了{dic['ad']}点血")
    dic = {
        'name': name,
        'sex': sex,
        'job': job,
        'level': level,
        'hp': hp,
        'weapon': weapon,
        'ad': ad,
        'action': cuo
    }
    return dic

def Dog(name,kind,hp,ad):
    def tian(person):
        person['hp'] -= dic['ad']
        print(f"{dic['name']}舔了{person['name']}，{person['name']}掉了{dic['ad']}点血")
    dic = {
        'name': name,
        'kind': kind,
        'hp': hp,
        'ad': ad,
        'action': tian
    }
    return dic


alex = Person('alex','不详','搓澡工',250,'搓澡巾',1)
wusir = Person('wusir','male','法师',500,'打狗棍',1000)
小白 = Dog('小白','泰迪',5000,249)
小金 = Dog('小金','柯基',10000,499)

小白['action'](wusir)

# 面向过程：想要一个结果 写代码 实现结果
# 面向对象：有哪些角色 角色的属性和方法 两个角色之间如何交互的

# 复杂的，拥有开放式结局的程序 比较适合使用面对对象开发
    # 游戏
    # 购物

















