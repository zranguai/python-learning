# 创建索引： create index 索引名 on 表（字段）;（例如:create index ind_id on s1(id);）
# 删除索引: drop index 索引名 on 表;


# 1.查询的条件字段不是索引字段，
# 对哪一个字段创建了索引，就用这个字段做条件查询
#
# 2.在创建索引的时候应该对区分度比较大的列进行创建
#     1/10以下的重复率比较适合创建索引
#
# 3.范围
#     范围越大越慢
#     范围越小越快
#     like 'a%' 快
#     like '%a' 慢
# 4.条件列参与计算/使用函数
#
# 5.and 和 or
#     id name（例如一个带索引，一个不带索引）
#         例子1：select * from s1 where id = 1800000 and name = 'eva';
#         例子2：select * from s1 where id = 1800000 or name = 'eva';
#     多个条件的组合,如果使用and连接
#     其中一列含有索引,都可以加快查找速度
#     如果使用or连接
#     必须所有的列都含有索引,才能加快查找速度
#
# 6.创建联合索引：最左前缀原则（必须到这最左边列做条件，从出现范围开始索引失效）
#     面试必考：
#         最左前缀原则：
#         (id,name,email):只要带着id就生效
#     例子：
#         select * from s1 where id = 1800000 and name = 'eval' and email = 'eval1800000@oldboy';
#         select * from s1 where id = 1800000 and name = 'eval';
#         select * from s1 where id = 1800000;


    # create index ind_mix on s1(id,name,email)


