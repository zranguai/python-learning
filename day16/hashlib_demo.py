"""7
    hashlib模块：md5加密算法
    给一个数据加密的三大步骤：
    1.获取一个加密对象
    2.使用加密对象的update进行加密，update方法可以调用多次
    3.通常通过hexdigest获取加密结果或者digest

"""
"""
    加密的目的：用于判断和验证，而并非解密
    特点：
    1.把一个大的数据，切分成不同块进行加密再汇总的结果，和直接对整体进行加密的结果是一样的
    2.单向加密，不可逆
    3.原始数据的一点小的变化，将导致结果非常大的差异。
"""

import hashlib
# 获取一个加密对象
# m = hashlib.md5()
# 使用加密对象的update，进行加密(参数是字节类型的参数)[后面还有就在前面的基础上再进行加密]
# m.update(b'abc')
# m.update('abc'.encode('utf-8'))
# m.update('中文'.encode('utf-8'))
# 通常通过hexdigest获取加密结果或者digest()方法（返回字节串）
# res = m.hexdigest()
# print(res)    # 1af98e0571f7a24468a85f91b908d335


"""
应用：验证
给一个数据加密：
验证：用例外一个数据加密的结果和第一次加密的结果对比
如果结果相同，说明原文相同
"""

# 不同加密算法：实际上就是加密结果的长度不同
# s = hashlib.sha224()
# s.update('abc中国'.encode('utf-8'))
# print(s.hexdigest())    # 8883193aef30cfd0744148ba80db834fddbdc141d2e70e47dfb95eb1

# 在创建加密对象时，可以指点参数，称为salt(加盐)
# m = hashlib.md5(b'abc')
# print(m.hexdigest())
#
# m1 = hashlib.md5()
# m1.update(b'abc')
# print(m1.hexdigest())


# 练习题：用加密算法实现登入注册
# 1：注册 2：登入 3 退出
def get_md5(username, password):
    m = hashlib.md5()
    m.update(username.encode('utf-8'))
    m.update(password.encode('utf-8'))
    return m.hexdigest()

def register(username, password):
    # 加密
    res = get_md5(username, password)
    # 写入文件
    with open('login', mode='at', encoding='utf-8') as f1:
        f1.write(res)
        f1.write('\n')
def login(username, password):
    # 加密
    res = get_md5(username, password)
    # 打开文件
    with open('login', mode='rt', encoding='utf-8') as f2:
        for line in f2:
            if res == line.strip():
                return True
            else:
                return False
while True:
    op = int(input('1：注册 2：登入 3 退出'))
    if op == 3:
        break
    elif op == 1:
        username = input('用户名')
        password = input('密码')
        register(username, password)
    elif op == 2:
        username = input('用户名')
        password = input('密码')
        res1 = login(username, password)
        if res1:
            print('登入成功')
        else:
            print('登入失败')

