# 约束某一个字段
# 无符号的 int unsigned
# 不能为空 not null
# 默认值  default
# 唯一约束 unique
#     联合唯一 unique(字段1,字段2)
# 自增 auto_increment
#     只能对数字有效.自带非空约束
#     至少是unique的约束之后才能使用auto_increment
# 主键 primary key
#     一张表只能有一个
#     如果不指定主键,默认是第一个非空+唯一
#     联合主键 primary key(字段1,字段2)
# 外键 Foreign key
#     Foreign key(自己的字段) references 外表(外表字段)
#     外表字段必须至少是"唯一"的




# create table t10(
#   id int unsigned
# );
#
# create table t11(
#   id int unsigned not null,
#   name char(18) not null
# );
#
# create table t12(
#   id int unsigned not null,
#   name char(18) not null,
#   male enum('male','female') not null default 'male'
# );

# 不能重复  unique   值不能重复,但是null可以写入多个
# create table t13(
#   id1 int unique,
#   id2 int
# )
#
# 联合唯一 unique
# create table t14(
#     id int,
#     server_name char(12),
#     ip char(15),
#     port char(5),
#     unique(ip,port)
# );
#
# 非空 + 唯一约束
# 第一个被定义为非空+唯一的那一列会成为这张表的primary key
# 一张表只能定义一个主键
# create table t15(
#     id int not null unique,
#     username char(18) not null unique
# );
# create table t16(
#     username char(18) not null unique,
#     id int not null unique
# );
# create table t17(
#     username char(18) not null unique,
#     id int primary key    # 指定主键，不指定的话非空+唯一的第一个就是主键
# )


# 联合主键（比较少用）
# create table t18(
#     id int,
#     server_name char(12),
#     ip char(15) default '',
#     port char(5) default '',
#     primary key(ip,port)
# );
#
# create table t19(
#     id int primary key,
#     server_name char(12),
#     ip char(15) not null,
#     port char(5) not null,
#     unique(ip,port)
# );


# 自增
# create table t20(
#     id int primary key auto_increment,
#     name char(12)
# );
# insert into t20(name) values('alex');

# 外键
# 班级表
# create table class(
#     cid int primary key auto_increment,
#     cname char(12) not null,
#     startd date
# )
'''
# 学生表
create table stu(
    id int primary key auto_increment,
    name char(12) not null,
    gender enum('male','female') default 'male',
    class_id int,
    foreign key(class_id) references class(cid)
)
'''

# create table stu2(
#     id int primary key auto_increment,
#     name char(12) not null,
#     gender enum('male','female') default 'male',
#     class_id int,
#     foreign key(class_id) references class(cid)
#     on update cascade
#     on delete cascade  # 尽量不用
# )



