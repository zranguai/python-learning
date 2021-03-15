# 用户相关操作：
# 查看当前用户是谁？select user();
# 给当前用户设置密码 set password = password('123');
# 创建用户：create user '用户名'@'主机的ip/主机域名' identified by '密码'
# 授权：grant select on 数据库名.* to '用户名'@'主机的ip/主机域名'

# 基础的库\表\数据操作
# 库 - 文件夹
    # 创建库             create database 数据库名;
    # 切换到这个库下     use 库名
    # 查看所有库         show databases;
# 表 - 文件
    # 查看这个库下的所有表  show tables;
    # 创建表                create table 表名(字段名 数据类型(长度),字段名 数据类型(长度),..);
    # 删除表                drop table 表名;
    # 查看表结构            desc 表名;
        # describe 表名;

# 数据(记录) - 文件中的内容
    # 增 : insert into 表 values (一行数据),(一行数据),(一行数据);
    # 删 : delete from 表 where 条件;
    # 改 : update 表 set 字段名=值,字段2=值2 where 条件;
    # 查 : select 字段 from 表;


