# python操作mysql数据库
import pymysql
# 1.连接数据库
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='',
                       database='homework')
# 2.获取游标
cur = conn.cursor()

# 3.执行sql语句
sql = 'select * from student'
cur.execute(sql)
for i in range(cur.rowcount):
    ret = cur.fetchone()
    print(ret)
print(ret)
cur.close()
conn.close()
