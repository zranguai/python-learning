# 环境变量
# python --> python.exe
# mysql默认端口3306

# 在任何目录下面都能够找到python.exe文件
# 才能在任意位置输入python命令启动python解释器


# mysqld install 安装mysql服务 mysql服务就被注册到操作系统中（已自动启动）
# net start mysql 启动mysql服务（之后开机都是自启动）
# net stop mysql 关闭mysql服务

# 先启动服务端 net start mysql(开机自启动)
# 再启动客户端 mysql -uroot -p（需要进程手动开启）
# 连接别人数据库 mysql -uroot -p123 -h192.168.14.12

# masql>select user();  查看当前用户是谁
# mysql>set password = password('123'); 给当前用户设置密码
#
# 创建一个其他用户
# mysql> create user 'guest'@'192.168.10.%'   IDENTIFIED BY '123';# 指示网段
# 给一个用户权限
# grant 权限类型(all,select,insert等)  on ftp.* to 'guest'@'192.168.14.%' (userinfo)
# grant all
# grant select
# grant select,insert

# mysql>flush privileges;    # 刷新使授权立即生效

# mysql>select user();
# 创建一个其他用户





# 操作数据库(文件夹)
# 查看所有数据库 show databases;
# 创建一个数据库 create database 数据库名;
# 切换到这个库下 use 数据库的名字;
# 查看这个库下有多少表 show tables;

# 操作表
# 创建一张表
# create table 表名(name char(12),age int);
# 查看表结构
# desc student;
#
# 操作数据
# 插入数据：insert into student values('alex',84);
# 查询数据: select * from student;
# 修改数据: update student set age=85 where name='alex';
# 删除数据: delete from student where name = 'alex';







