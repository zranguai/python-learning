# 1.写一个注册登入 基于数据库来做
    # 加上hashlib密文验证
import pymysql
import hashlib
username = input('username:')
password = input('password:')
# 输入加密：
def m5(username, password):
    m1 = hashlib.md5()
    m1.update(username.encode('utf-8'))
    res1 = m1.hexdigest()

    m2 = hashlib.md5()
    m2.update(password.encode('utf-8'))
    res2 = m2.hexdigest()
    return res1, res2
def mysql():
    # 1.连接数据库
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='',
                           database='day42')
    # 2.获取游标
    cur = conn.cursor()
    # 3.sql语句
    sql = 'select user,password from userinfo'
    # 4.执行sql语句
    cur.execute(sql)
    # 5.获取结果
    ret = cur.fetchone()
    return ret[0],ret[1]

my = mysql()

# 判断输入的用户名和密码是否和输入的用户名密码一致
def login():
    m1 = my[0]
    m2 = my[1]
    result1 = m5(m1, m2)
    result2 = m5(username, password)
    if result1 == result2:
        print('登入成功')
        return True
    else:
        print('用户名或密码错误')
        return False

login()
# 2.例外10道题
