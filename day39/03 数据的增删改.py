# create table t1(
#     id int primary key auto_increment,
#     username char(12) not null,
#     sex enum('male','female') default 'male',
#     hobby set('上课','写作业','考试') not null
# )

# 增 insert into 表(字段) values(值...);
# insert into t1 values(1,'大壮','male','上课,写作业');
# insert into t1 values(2,'小明','male','考试,写作业');
# insert into t1 values(3,'小红','male','写作业'),(4,'小华','male','考试');
# insert into t1(username,hobby) values('小刚','上课,写作业,考试');

# 把别的表查询的结果写进自己表中
# create table t2(id int, name char(12));
# insert into t2 (id,name) select id,username from t1;
# mysql> select * from t2;
# +------+--------+
# | id   | name   |
# +------+--------+
# |    1 | 大壮   |
# |    2 | 小明   |
# |    3 | 小红   |
# |    4 | 小华   |
# |    5 | 小刚   |
# +------+--------+


# 删
# delete from t2    # 删除整张表
#     会清空表,但是不会清空自增字段的offset(偏移量)值
#     truncate table 表:
#         会清空表和自增字段的偏移量
# 删除某一条数据
#     delete from 表 where 条件;


# 改
#     update 表 set 字段=值 where 条件
#     update 表 set 字段=值,字段=值 where 条件


# 10个查询 1个增删改
























