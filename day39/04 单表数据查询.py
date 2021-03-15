# 建表和数据准备
# 创建表
# create table employee(
# id int not null unique auto_increment,
# emp_name varchar(20) not null,
# sex enum('male','female') not null default 'male', #大部分是男的
# age int(3) unsigned not null default 28,
# hire_date date not null,
# post varchar(50),
# post_comment varchar(100),
# salary double(15,2),
# office int, #一个部门一个屋子
# depart_id int
# );

# 插入记录
# 三个部门：教学，销售，运营
# insert into employee(emp_name,sex,age,hire_date,post,salary,office,depart_id) values
# ('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33,401,1), #以下是教学部
# ('alex','male',78,'20150302','teacher',1000000.31,401,1),
# ('wupeiqi','male',81,'20130305','teacher',8300,401,1),
# ('yuanhao','male',73,'20140701','teacher',3500,401,1),
# ('liwenzhou','male',28,'20121101','teacher',2100,401,1),
# ('jingliyang','female',18,'20110211','teacher',9000,401,1),
# ('jinxin','male',18,'19000301','teacher',30000,401,1),
# ('成龙','male',48,'20101111','teacher',10000,401,1),
#
# ('歪歪','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
# ('丫丫','female',38,'20101101','sale',2000.35,402,2),
# ('丁丁','female',18,'20110312','sale',1000.37,402,2),
# ('星星','female',18,'20160513','sale',3000.29,402,2),
# ('格格','female',28,'20170127','sale',4000.33,402,2),
#
# ('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
# ('程咬金','male',18,'19970312','operation',20000,403,3),
# ('程咬银','female',18,'20130311','operation',19000,403,3),
# ('程咬铜','male',18,'20150411','operation',18000,403,3),
# ('程咬铁','female',18,'20140512','operation',17000,403,3)
# ;

# 简单查询:
# 1.select语句
# 最简单的select*****
#     select * from 表;
#     select 字段,... from 表;
# 重命名字段 *****   # 原表里的名字不会变,但是查询出来的名字变成你改的名字
#     select 字段1 as 新名字1,字段2 as 新名字2,... from 表;
#     select 字段1 新名字1,字段2 新名字2,... from 表;
# 去重 ****
#     select distinct 字段 from 表;
#     select distinct age,sex from employee;
# 使用函数 ****
#     concat:   SELECT CONCAT('姓名: ',emp_name,'  年薪: ', salary*12)  AS Annual_salary FROM employee;
#
#     concat_ws,第一个为分隔符SELECT CONCAT_WS(':',emp_name,salary*12)  AS Annual_salary FROM employee;


# 四则运算的
#      select emp_name,salary*12 from employee; 乘法
#      select emp_name,salary*12 as annual_salary from employee;
# 使用判断逻辑
#     case when语句 相当于 if条件判断句
#         结合CASE语句：
#         SELECT
#         (
#             CASE
#             WHEN emp_name = 'jingliyang' THEN
#             emp_name
#             WHEN emp_name = 'alex' THEN
#             CONCAT(emp_name, '_BIGSB')
#         ELSE
#         concat(emp_name, 'SB')
#         END
#         ) as new_name
#         FROM
#         employee;


# where 筛选所有符合条件的行
#     比较运算符
#         > < >= <= <> !=
#     范围
#         between 10000 and 20000 要1w-2w之间的
#         in (10000,20000)   只要10000或者20000的
#     模糊匹配
#         like
#             % 通配符 表示任意长度的任意内容
#             _ 通配符 一个字符长度的任意内容
#         regexp
#             '^a'
#             'g$'
#     逻辑运算
#         not\and\or
#
# 注意:# 查看岗位描述不为NULL的员工信息
#         is
#         select * from employee where post_comment is not null;




# 分组 group by 根据谁分组,可以求这个组的总人数,最大值,最小值,平均值,求和 但是这个求出来的值只是和分组字段对应
#     并不和其他任何字段对应,这个时候查出来的所有其他字段都不生效.
# 聚合函数
#     count 求个数
#     max  求最大值
#     min  求最小值
#     sum  求和
#     avg  求平均
#
# 只能看,不能取值
# SELECT post,emp_name FROM employee GROUP BY post;
#     SELECT post,GROUP_CONCAT(emp_name) FROM employee GROUP BY post;


# having 过滤语句
#     在having条件中可以使用聚合函数,在where中不行
#     适合去筛选符合条件的某一组数据,而不是某一行数据
#     先分组再过滤 : 求平均薪资大于xx的部门,求人数大于xx的性别,求大于xx人的年龄段
# 查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
# group by post having count(id) < 2;
#
# 排序 order by
#     默认是升序  asc
#     降序  desc
#     order by age ,salary desc
#         优先根据age从小到大排,在age相同的情况下,再根据薪资从大到小排
#
# limit m,n
#     从m+1项开始,取n项
#     如果不写m,m默认为0
#
#     limit n offset m