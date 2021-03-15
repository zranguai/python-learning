# MySql
## part 1:
### 数据库概念
+ 数据库：（DataBase, 简称DB）:数据库中的数据按一定的数据模型组织、描述和储存，具有较小的冗余度、较高的数据独立性和易扩展性，并可为各种 用户共享
+ 数据库管理系统（DataBase Management System 简称DBMS）：
+ 数据库服务器：一台计算机（对内存要求比较高）
+ 数据库管理系统：如mysql(是一个软件)
+ 数据库：db（即文件夹）
+ 表：userinfo, studentinfo,courseinfo(即文件)
+ 记录：1 朱葛 13234567890 22（多个字段的信息组成一条记录，即文件中的一行内容）
+ 总结：
+ 数据库服务器：运行数据库管理软件
+ 数据库管理软件：管理-数据库
    1. 数据库：即：文件夹，用来组织文件/表
	2. 表：即文件，用来存放多行内容/多条记录
+ 记录：即文件中的一行内容
+ 关系型数据库   相对慢
+ 非关系型数据库 块
    + 快递 快递单号
    + 视频 电影的id: 电影的内容
### mysql的账号操作
```
mysqld install 安装mysql服务 mysql服务就被注册到操作系统中（已自动启动）
net start mysql 启动mysql服务（之后开机都是自启动）
net stop mysql 关闭mysql服务

先启动服务端 net start mysql(开机自启动)
再启动客户端 mysql -uroot -p（需要自己手动开启）[以root身份进入]
连接别人数据库 mysql -uroot -p123 -h192.168.14.12
```
```
进入mysql客户端
$mysql
mysql>select user();    # 查看当前用户
mysql> exit     # 也可以用\q quit退出
# 默认用户登陆之后并没有实际操作的权限
# 需要使用管理员root用户登陆
$ mysql -uroot -p   # mysql5.6默认是没有密码的
#遇到password直接按回车键
mysql> set password = password('root'); # 给当前数据库设置密码
```
```
# 创建账号：
mysql> create user 'eva'@'192.168.10.%'   IDENTIFIED BY '123';# 指示网段
mysql> create user 'eva'@'192.168.10.5'   # 指示某机器可以连接
mysql> create user 'eva'@'%'                    #指示所有机器都可以连接 
mysql> show grants for 'eva'@'192.168.10.5';查看某个用户的权限
```
```
# 远程登入
$ mysql -uroot -p123 -h 192.168.10.3

# 给账号授权
mysql> grant all[可选all,select,insert等] on *.* to 'eva'@'%';
{例如：# grant 权限类型(all,select,insert等)  on ftp.* to 'guest'@'192.168.14.%' (userinfo)}
mysql> flush privileges;    # 刷新使授权立即生效

# 创建账号并授权
mysql> grant all on *.* to 'eva'@'%' identified by '123' 
```
### mysql基础
```
操作数据库(文件夹)
查看所有数据库 show databases;
创建一个数据库 create database 数据库名;
切换到这个库下 :use 数据库的名字;
查看这个库下有多少表: show tables;

操作表
创建一张表
create table 表名(name char(12),age int);
查看表结构
desc student;

操作数据
插入数据：insert into student values('alex',84);
查询数据: select * from student;
修改数据: update student set age=85 where name='alex';
删除数据: delete from student where name = 'alex';
```
1. 操作文件夹（库）
```
增：create database db1 charset utf8;
查：show databases;
改：alter database db1 charset latin1;
删除: drop database db1;
```
2. 操作文件（表）
```
先切换到文件夹下：use db1
增：create table t1(id int,name char);
查：show tables;
改：alter table t1 modify name char(3);
   alter table t1 change name name1 char(2);
删：drop table t1;
```
3. 操作文件中的内容（记录）
```
增：insert into t1 values(1,'egon1'),(2,'egon2'),(3,'egon3');
查：select * from t1;
改：update t1 set name='sb' where id=2;
删：delete from t1 where id=1;
```
4. 清空表：
```
delete from t1; #如果有自增id，新增的数据，仍然是以删除前的最后一样作为起始。
truncate table t1;数据量大，删除速度比上一条快，且直接从零开始，

*auto_increment 表示：自增
*primary key 表示：约束（不能重复且不能为空）；加速查找
```
## part2:
### 存储引擎
**存储数据的方式**

1. Innodb存储引擎 *****    mysql5.6之后的默认的存储引擎
+ 数据和索引存储在一起 2个文件
    + 数据索引\表结构
+ 数据持久化

+ 支持事务   : 为了保证数据的完整性,将多个操作变成原子性操作   : 保持数据安全
+ 支持行级锁 : 修改的行少的时候使用                          : 修改数据频繁的操作
+ 支持表级锁 : 批量修改多行的时候使用                        : 对于大量数据的同时修改
+ 支持外键   : 约束两张表中的关联字段不能随意的添加\删除      : 能够降低数据增删改的出错率

2. Myisam存储引擎    mysql5.5之前的默认的存储引擎
+ 数据和索引不存储在一起  3个文件
    + 数据\索引\表结构
+ 数据持久化
+ 只支持表锁

3. Memory存储引擎
+ 数据存储在内存中, 1个文件
    + 表结构
+ 数据断电消失

**查看存储引擎：show engines;**

+ 面试题
```
你了解mysql的存储引擎么?
你的项目用了什么存储引擎,为什么?
    innodb
    多个用户操作的过程中对同一张表的数据同时做修改
    innodb支持行级锁,所以我们使用了这个存储引擎
    为了适应程序未来的扩展性,扩展新功能的时候可能会用到...,涉及到要维护数据的完整性
    项目中有一两张xx xx表,之间的外键关系是什么,一张表的修改或者删除比较频繁,怕出错所以做了外键约束
```
### 表和数据的基本操作
1. 创建表：
```
create table 表名(
	id int,
	name char(18),
	字段名3 类型[(宽度) 约束条件]
);
放在中括号里的内容可以不写
```
2. 写入数据的方式（三种方式）：
```
insert into 表 values (值1,值2,值3);
    这张表有多少的字段,就需要按照字段的顺序写入多少个值
insert into 表 values (值1,值2,值3),(值1,值2,值3),(值1,值2,值3);
    一次性写入多条数据
insert into 表 (字段1,字段3 ) values (值1,值3);
    指定字段名写入,可以任意的选择表中你需要写入的字段进行
```
3. 查表中的数据：

    ```  select * from 表```

4. 查看表结构：
```
    desc 表名;（更加利于查看）
        能够查看到有多少个字段\类型\长度,看不到表编码,引擎,具体的约束信息只能看到一部分
    show create table 表名;
        能查看字段\类型\长度\编码\引擎\约束
```
### 数据类型--数字
+ int 不约束长度，最多表示10位数
+ float(m,n)
    + m 一共多少位
    + n 小数部分多少位
+ 例子：
```
创建表：
create table t1(
    id int,    # 默认是有符号的{一般使用int 类型}
    age tinyint unsigned    # 如果需要定义无符号的使用unsigned[表示非负数]
)

create table t2(
    f1 float(5,2),    # 保留两位小数，并且四舍五入。 一共5位数，后面小数的位数未2位，前面为3位数。
    f2 float          # 大部分使用float即可满足要求
    f3 double(5,2),
    f4 double
)
```
### 数据类型--时间
+ date          20190620
+ time          121953
+ datetime  20190620121953
+ year
+ date
+ time
+ timestamp
+ **例子：**
```
create table t4(
    dt  datetime,
    y  year,
    d  date,
    t  time,
    ts  timestamp
);

mysql> create table t5(
    -> id int,
    -> dt datetime NOT NULL                        # 不能为空
                  DEFAULT CURRENT_TIMESTAMP        # 默认是当前时间
                  ON UPDATE CURRENT_TIMESTAMP);    # 在更新的时候使用当前时间更新字段
```
### 数据类型--字符串
+ char
+ varchar
```
char(18)    # 最多只能表示255个字符
    定长存储，浪费空间，节省时间
    'alex'    'alex           '
varchar(18) # 最多能表示65535个字符
    变长存储，更节省空间,存取速度慢
    'alex'     'alex4'
```
```
适合使用char
    身份证号
    手机号码
    qq号
    username 12-18
    password 10-16
    银行卡号

适合使用varchar
    评论
    朋友圈
    微博
```
+ 例子：
```
建表
create table t6(
    c1 char,             # 默认长度是1
    v1 varchar(1),    # 必须写长度
    c2 char(8),
    v2 varchar(8)
);
```
### 数据类型--enum和set
+ enum 单选
+ set 多选
+ 例子：
```
create table t8(
    id int,
    name char(18),
    gender enum('male','female')
);

create table t9(
    id int,
    name char(18),
    hobby set('抽烟','喝酒','烫头')
);

insert into t9 values (1,'alex','抽烟，喝酒');
```
### 表的完整性约束
+ 约束某一个字段
+ 无符号的 int unsigned        {unsigned表示非负数}
+ 不能为空 not null
+ 默认值  default
+ 唯一约束 unique
    + 联合唯一 unique(字段1,字段2)
+ 自增 auto_increment
    + 只能对数字有效.自带非空约束
    + 至少是unique的约束之后才能使用auto_increment
+ 主键 primary key
    + 一张表只能有一个
    + 如果不指定主键,默认是第一个非空+唯一
    + 联合主键 primary key(字段1,字段2)
+ 外键 foreign key
    + Foreign key(自己的字段) references 外表(外表字段)
    + 外表字段必须至少是"唯一"的
- 例子：
```
create table t10(
  id int unsigned
);

create table t11(
  id int unsigned not null,
  name char(18) not null
);

create table t12(
  id int unsigned not null,
  name char(18) not null,
  male enum('male','female') not null default 'male'
);
```
+ 不能重复  unique   值不能重复,但是null可以写入多个
```
create table t13(
  id1 int unique,
  id2 int
)
```
+ 联合唯一 unique
```
create table t14(
    id int,
    server_name char(12),
    ip char(15),
    port char(5),
    unique(ip,port)
);
```
+ 非空 + 唯一约束
```
第一个被定义为非空+唯一的那一列会成为这张表的primary key
一张表只能定义一个主键
create table t15(
    id int not null unique,
    username char(18) not null unique
);
create table t16(
    username char(18) not null unique,
    id int not null unique
);
create table t17(
    username char(18) not null unique,
    id int primary key    # 指定主键，不指定的话非空+唯一的第一个就是主键
)
```
+ 联合主键（比较少用）
```
create table t18(
    id int,
    server_name char(12),
    ip char(15) default '',
    port char(5) default '',
    primary key(ip,port)
);

create table t19(
    id int primary key,
    server_name char(12),
    ip char(15) not null,
    port char(5) not null,
    unique(ip,port)
);
```
+ 自增
```
create table t20(
    id int primary key auto_increment,
    name char(12)
);
insert into t20(name) values('alex');
```
+ 外键
```
班级表
create table class(
    cid int primary key auto_increment,
    cname char(12) not null,
    startd date
)

# 学生表
create table stu(
    id int primary key auto_increment,
    name char(12) not null,
    gender enum('male','female') default 'male',
    class_id int,
    foreign key(class_id) references class(cid)
)

create table stu2(
    id int primary key auto_increment,
    name char(12) not null,
    gender enum('male','female') default 'male',
    class_id int,
    foreign key(class_id) references class(cid)
    on update cascade
    on delete cascade  # 尽量不用
)
```
### 表与表之间的关系
+ 分析步骤：
1. 先站在左表的角度去找
是否左表的多条记录可以对应右表的一条记录，如果是，则证明左表的一个字段foreign key 右表一个字段（通常是id）

2. 再站在右表的角度去找
是否右表的多条记录可以对应左表的一条记录，如果是，则证明右表的一个字段foreign key 左表一个字段（通常是id）

3. 总结：
+ 多对一：
  + 如果只有步骤1成立，则是左表多对一右表
  + 如果只有步骤2成立，则是右表多对一左表

+ 多对多
    + 如果步骤1和2同时成立，则证明这两张表时一个双向的多对一，即多对多,需要定义一个这两张表的关系表来专门存放二者的关系

+ 一对一:
    + 如果1和2都不成立，而是左表的一条记录唯一对应右表的一条记录，反之亦然。这种情况很简单，就是在左表foreign key右表的基础上，将左表的外键字段设置成unique即可
