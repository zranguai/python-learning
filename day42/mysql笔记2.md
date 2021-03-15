# MySql笔记2：
## part3:(table相关的操作)
### 数据的增删改
```
create table t1(
    id int primary key auto_increment,
    username char(12) not null,
    sex enum('male','female') default 'male',
    hobby set('上课','写作业','考试') not null
)
```
1. 增 insert into 表(字段) values(值...);
```
insert into t1 values(1,'大壮','male','上课,写作业');
insert into t1 values(2,'小明','male','考试,写作业');
insert into t1 values(3,'小红','male','写作业'),(4,'小华','male','考试');
insert into t1(username,hobby) values('小刚','上课,写作业,考试');
```
+ 把别的表查询的结果写进自己表中
```
create table t2(id int, name char(12));
insert into t2 (id,name) select id,username from t1;
mysql> select * from t2;
+------+--------+
| id   | name   |
+------+--------+
|    1 | 大壮   |
|    2 | 小明   |
|    3 | 小红   |
|    4 | 小华   |
|    5 | 小刚   |
+------+--------+
```
2. 删
```
delete from t2    # 删除整张表
    会清空表,但是不会清空自增字段的offset(偏移量)值
    truncate table 表:
        会清空表和自增字段的偏移量
删除某一条数据
    delete from 表 where 条件;
```
3. 改
```
update 表 set 字段=值 where 条件
update 表 set 字段=值,字段=值 where 条件
```
### 数据的查询
1. select语句
+ 最简单的select*****
```
select * from 表;
select 字段,... from 表;
```
+ 重命名字段 *****   # 原表里的名字不会变,但是查询出来的名字变成你改的名字
```
select 字段1 as 新名字1,字段2 as 新名字2,... from 表;
select 字段1 新名字1,字段2 新名字2,... from 表;
```
+ 去重 ****
```
select distinct 字段 from 表;
select distinct age,sex from employee;
```
+ 使用函数 ****
```
concat:   SELECT CONCAT('姓名: ',emp_name,'  年薪: 'salary*12)  AS Annual_salary FROM employee;

concat_ws,第一个为分隔符SELECT CONCAT_WS(':',emp_namsalary*12)  AS Annual_salary FROM employee;
```
+ 四则运算的
```
select emp_name,salary*12 from employee; 乘法
select emp_name,salary*12 as annual_salary from employee;
```
+ 使用判断逻辑
```
    case when语句 相当于 if条件判断句
        结合CASE语句：
        SELECT
        (
            CASE
            WHEN emp_name = 'jingliyang' THEN
            emp_name
            WHEN emp_name = 'alex' THEN
            CONCAT(emp_name, '_BIGSB')
        ELSE
        concat(emp_name, 'SB')
        END
        ) as new_name
        FROM
        employee;
```
### where约束
```
where 筛选所有符合条件的行
    比较运算符
        > < >= <= <> !=
    范围
        between 10000 and 20000 要1w-2w之间的
        in (10000,20000)   只要10000或者20000的
    模糊匹配
        like
            % 通配符 表示任意长度的任意内容
            _ 通配符 一个字符长度的任意内容
        regexp
            '^a'
            'g$'
    逻辑运算
        not\and\or      {优先级从高到底}

注意:# 查看岗位描述不为NULL的员工信息
        is
        select * from employee where post_comment is not null;
```
### group by 分组
```
分组 group by 根据谁分组,可以求这个组的总人数,最大值,最小值,平均值,求和 但是这个求出来的值只是和分组字段对应
    并不和其他任何字段对应,这个时候查出来的所有其他字段都不生效.
聚合函数
    count 求个数
    max  求最大值
    min  求最小值
    sum  求和
    avg  求平均

只能看,不能取值
SELECT post,emp_name FROM employee GROUP BY post;
    SELECT post,GROUP_CONCAT(emp_name) FROM employee GROUP BY post;
```
### having过滤语句/order by排序/limit
```
having 过滤语句:(通常与group by 一起用)
    在having条件中可以使用聚合函数,在where中不行
    适合去筛选符合条件的某一组数据,而不是某一行数据
    先分组再过滤 : 求平均薪资大于xx的部门,求人数大于xx的性别,求大于xx人的年龄段
查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
group by post having count(id) < 2;

排序 order by
    默认是升序  asc
    降序  desc
    order by age ,salary desc
        优先根据age从小到大排,在age相同的情况下,再根据薪资从大到小排

limit m,n（从m+1项开始取n项）
    从m+1项开始,取n项
    如果不写m,m默认为0

    limit n offset m
```
## part4:(连表查询，子查询)
### 连表查询
+ 使用文件信息：source  文件路径
+ 如果一个问题既可以使用连表查询解决也可以使用子查询解决
推荐使用连表查询,因为效率高
1. where条件中不能用select字段的重命名
2. order by 或者having可以使用select字段的重命名
    + 主要是因为order by 在select语句之后才执行
    + having经过了mysql的特殊处理,使得它能够感知到select语句中的重命名

    + 拓展
        + 在执行select语句的时候,实际上是通过where,group by,having这几个语句锁定对应的行
        + 然后循环每一行执行select语句
+ 所谓连接
    + 总是在连接的时候创建一张大表,里面存放的是两张表的笛卡尔积
    + 再根据条件进行筛选就可以了
+ **表与表之间的连接方式**
+ select * from 表1,表2 where 条件  (了解即可)
1. 内连接 inner join...on...*****
```
select * from 表1 inner join 表2 on 条件
    例如:select * from department inner join employee on department.id = employee.dep_id;
    起别名:select * from department as t1 inner join employee as t2 on t1.id = t2.dep_id;
```
2. 外连接
```
    左外连接 left join...on...(*****)
        select * from 表1 left join 表2 on 条件
            例子: select * from department as t1 left join employee as t2 on t1.id = t2.dep_id;
    右外连接 right join...on...
        select * from 表1 right join 表2 on 条件
            例子: select * from department as t1 right join employee as t2 on t1.id = t2.dep_id;
    全外连接 full join (不太常用)
        select * from department as t1 left join employee a t2 on t1.id = t2.dep_id
        union
        select * from department as t1 right join employee a t2 on t1.id = t2.dep_id;

所谓连表就是把两张表连接在一起之后 就变成一张大表  从from开始一直到on条件结束就看做一张表
之后 where 条件 group by 分组 order by limit 都正常的使用就可以了
```
### 
+ 子查询
```
#1：子查询是将一个查询语句嵌套在另一个查询语句中。
#2：内层查询语句的查询结果，可以为外层查询语句提供查询条件。
#3：子查询中可以包含：IN、NOT IN、ANY、ALL、EXISTS 和 NOT EXISTS等关键字
#4：还可以包含比较运算符：= 、 !=、> 、<等
```
### 数据查询加载顺序
![数据查询加载顺序](https://img-blog.csdnimg.cn/20201030190037966.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTAzNjk0NA==,size_16,color_FFFFFF,t_70#pic_center)

## part5:MySql索引原理
### MySql索引原理简介
+ mysql中存储数据的两种方式
    + 聚集索引
    + 非聚集索引

+ 索引的创建与删除
    + 创建主键 primary key 聚集索引 + 非空+ 唯一
    + 创建唯一约束 unique 辅助索引 + 唯一
    + 添加一个普通索引(一般是已经创建好了表查询的时候发现慢，就加上索引)
        + 创建索引： create index 索引名 on 表（字段）;
        + （例如:create index ind_id on s1(id);）
        + 删除索引: drop index 索引名 on 表;
+ 索引
    + 创建
    + 删除
    + 知道用了它会加快查询的速度
### 索引结构--树
+ root 根节点
+ branch 分支节点
+ leaf 叶子节点
+ 父子节点
+ 二叉树

+ 平衡树不一定是二叉树
+ b+树*****
    + 平衡树 能够让查找某一个值经历的查找速度尽量平衡  balance tree
    + 分支节点不存储数据--让树的高度尽量矮，让查找一个数据的效率尽量的稳定
    + 在所有的叶子节点加入了双向的地址链接--查找范围非常快
+ 为什么不用二叉树
+ 两种索引的差别（叶子节点存储具体数据，叶子节点不存储具体数据）

+ 聚集索引 聚簇索引
    + Innodb 必有且仅有一个:主键
    + innodb存储引擎中的 主键默认就会创建一个据集索引
+ 非聚集索引 辅助索引
    + innodb
    + myisam
+ **聚集索引与非聚集索引**
![聚集索引与非聚集索引](https://img-blog.csdnimg.cn/20201030191030833.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTAzNjk0NA==,size_16,color_FFFFFF,t_70#pic_center)
### **正确的使用索引**
+ 创建索引： create index 索引名 on 表（字段）;（例如:create index ind_id on s1(id);）
+ 删除索引:    drop index 索引名 on 表;
1. 查询的条件字段不是索引字段，
    + 对哪一个字段创建了索引，就用这个字段做条件查询

2. 在创建索引的时候应该对区分度比较大的列进行创建
    + 1/10以下的重复率比较适合创建索引

3. 范围
    + 范围越大越慢
    + 范围越小越快
    + like 'a%' 快
    + like '%a' 慢

4. 条件列参与计算/使用函数

5. and 和 or
    + id name（例如一个带索引，一个不带索引）
        + 例子1：select * from s1 where id = 1800000 and name = 'eva';
        + 例子2：select * from s1 where id = 1800000 or name = 'eva';
    + 多个条件的组合,如果使用and连接
        + 其中一列含有索引,都可以加快查找速度
    + 如果使用or连接
        + 必须所有的列都含有索引,才能加快查找速度

6. 创建联合索引：最左前缀原则（必须到这最左边列做条件，从出现范围开始索引失效）
    + **面试必考**：
        + 最左前缀原则：
        + (id,name,email):只要带着id就生效
    + 例子：
        + select * from s1 where id = 1800000 and name = 'eval' and email = 'eval1800000@oldboy';
        + select * from s1 where id = 1800000 and name = 'eval';
        + select * from s1 where id = 1800000;
## part6:python操作mysql
### python操作数据库
```
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
```
### pymysql模块和查
+ 步骤：
	+ pymysql
	    + python操作mysql数据库
            1. 连接数据库
	        2. 获取游标
	        3. 执行sql(增删改查)
	        4. 如果涉及到修改：需要提交
	        5. 关闭游标
	        6. 关闭库
	    + sql注入
	        + 传参数,注意sql注入的问题，传参数通过execute方法来传
        + 例如：execute('select * from 表 where name = %s',('alex',))
+ 事务：
```
begin;  # 开启事务
select * from emp where id = 1 for update;  # 查询id值，for update添加行锁；
update emp set salary=10000 where id = 1; # 完成更新
commit; # 提交事务
```
+ 例子：
```
import pymysql
连上数据库
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password="",
                       database='homework')
# 拿到游标
# cur = conn.cursor()    # cursor游标  默认形式
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)    # 以字典的形式拿到数据


try:
    cur.execute('select * from student')
    # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数
    ret = cur.fetchone()    # 每次拿一个
    print(ret)
    ret2 = cur.fetchmany(10)    # 获取多条结果
    print(ret2)
    ret3 = cur.fetchall()    # 获取全部结果
    print(ret3)
except pymysql.err.ProgrammingError as e:
    print(e)


cur.close()
conn.close()
```
### pymysql模块之增加/删除/修改
+ **增加 删除 和修改：需要commit**
```
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='',
                       database='homework')
cur = conn.cursor()    # cursor游标

try:
    # cur.execute('insert into student values(18,"男",3,"大壮")')
    # cur.execute('update student set gender="女" where sid=17')
    cur.execute('delete from student where sid=17')
    conn.commit()    # 从内存中写入数据库中
except Exception as e:
    print(e)
    conn.rollback()    # 回滚 之前写的代码都不执行了
cur.close()
conn.close()
```
+ sql注入问题：传参数,注意sql注入的问题，传参数通过execute方法来传
```
实际操作mysql的时候会遇到的一个问题

结合数据库和python写一个登入
username password
 alex     3714


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
cur.execute(sql,(user,pwd))
print(cur.fetchone())
```
### 数据备份和恢复
```
路径：D:\python_22\day42\tmp.sql

表和数据的备份
    备份数据
    再cmd命令行直接执行
    mysqldump -uroot -p123 -h1270.0.0.1 homework > D:\python_22\day42\tmp.sql

    恢复数据 再mysql中执行命令
    切换到一个要备份的数据库中
    source D:\python_22\day42\tmp.sql

备份库
    备份
    mysqldump -uroot -p123 --databases homework > D:\python_22\day42\tmp2.sql
    恢复
    source source D:\python_22\day42\tmp2.sql
```
