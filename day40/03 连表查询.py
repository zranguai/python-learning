# 所谓连接
#     总是在连接的时候创建一张大表,里面存放的是两张表的笛卡尔积
#     再根据条件进行筛选就可以了
#
# 表与表之间的连接方式
#     select * from 表1,表2 where 条件  (了解即可)
#     内连接 inner join...on...*****
#     select * from 表1 inner join 表2 on 条件
#         例如:select * from department inner join employee on department.id = employee.dep_id;
#         起别名:select * from department as t1 inner join employee as t2 on t1.id = t2.dep_id;
#
#     外连接
#         左外连接 left join...on...(*****)
#             select * from 表1 left join 表2 on 条件
#                 例子: select * from department as t1 left join employee as t2 on t1.id = t2.dep_id;
#         右外连接 right join...on...
#             select * from 表1 right join 表2 on 条件
#                 例子: select * from department as t1 right join employee as t2 on t1.id = t2.dep_id;
#         全外连接 full join (不太常用)
#             select * from department as t1 left join employee as t2 on t1.id = t2.dep_id
#             union
#             select * from department as t1 right join employee as t2 on t1.id = t2.dep_id;
#
#
# 所谓连表就是把两张表连接在一起之后 就变成一张大表  从from开始一直到on条件结束就看做一张表
# 之后 where 条件 group by 分组 order by limit 都正常的使用就可以了

# 练习:
# 1.找到技术部的所有人的名字
# 2.找到人力资源部的年龄大于40岁的人的名字

