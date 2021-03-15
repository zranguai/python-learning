import pymysql
# 连上数据库
# conn = pymysql.connect(host='127.0.0.1',
#                        user='root',
#                        password="",
#                        database='homework')
# # 拿到游标
# # cur = conn.cursor()    # cursor游标  默认形式
# cur = conn.cursor(cursor=pymysql.cursors.DictCursor)    # 以字典的形式拿到数据
#
#
# try:
#     cur.execute('select * from student')
#     # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数
#     ret = cur.fetchone()    # 每次拿一个
#     print(ret)
#     ret2 = cur.fetchmany(10)    # 获取多条结果
#     print(ret2)
#     ret3 = cur.fetchall()    # 获取全部结果
#     print(ret3)
# except pymysql.err.ProgrammingError as e:
#     print(e)
#
#
# cur.close()
# conn.close()



# 增加 删除 和修改
# conn = pymysql.connect(host='127.0.0.1',
#                        user='root',
#                        password='',
#                        database='homework')
# cur = conn.cursor()    # cursor游标
#
# try:
#     # cur.execute('insert into student values(18,"男",3,"大壮")')
#     # cur.execute('update student set gender="女" where sid=17')
#     cur.execute('delete from student where sid=17')
#     conn.commit()    # 从内存中写入数据库中
# except Exception as e:
#     print(e)
#     conn.rollback()    # 回滚 之前写的代码都不执行了
# cur.close()
# conn.close()




# 实际操作mysql的时候会遇到的一个问题

# 结合数据库和python写一个登入
# username password
# alex     3714
user = input('username:')
pwd = input('password:')
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='',
                       database='day42')
cur = conn.cursor()    # cursor游标
# sql = f'select * from userinfo where user="{user}" and password="{pwd}"'
# sql = 'select * from userinfo where user="%s" and password="%s";'%(user,pwd)
sql = 'select * from userinfo where user = %s and password = %s'    # 改进版
print(sql)
cur.execute(sql, (user, pwd))
print(cur.fetchone())



# sql注入
# select * from userinfo where user="alex";--" and password="3714"
# select * from userinfo where user="1869" or 1=1;" and password="3714"

