# b+树
    # b是balance 平衡的意思
        # 为了保证每一个数据查找经历的IO次数都相同
    # 只在叶子节点存储数据
        # 为了降低树的高度
    # 叶子节点之前加入了双向连接
        # 为了查找范围的时候比较快

# 聚集索引(聚簇索引)
    # 全表数据都存储在叶子节点上 -- Innodb存储引擎中的主键
# 非聚集索引(非聚簇索引)/辅助索引
    # 叶子节点不存放具体的整行数据,而是存储的这一行的主键的值

# 索引的创建和删除
    # create index ind_name on 表名(字段名);
    # create index ind_name on 表名(字段名,字段2);
    # drop index 索引名 on 表名

# 正确的使用mysql数据库
    # 从库的角度
        # 搭建集群
        # 读写分离
        # 分库
    # 从表的角度
        # 合理安排表与表之间的关系 :该拆的拆,该合的合
        # 把固定长度的字段放在前面
        # 尽量使用char而不是varchar
    # 从操作数据的角度
        # 尽量在where字段就约束数值到一个比较小的范围 : 分页
            # where a between value1 and value2
        # 尽量使用连表查询代替子查询
        # 删除数据和修改数据的时候条件尽量使用主键
        # 合理的创建和使用索引
            # 创建索引
                # 1.选择区分度比较大的列
                # 2.尽量选择短的字段创建索引
                # 3.不要创建不必要的索引,及时删除不用的索引
            # 使用索引
                # 1.查询的字段不是索引字段
                # 2.在条件中使用范围,结果的范围越大速度越慢,范围小就快
                # 3.like 'a%'命中索引,like '%a'不命中索引
                # 4.条件列不能参与计算\不能使用函数
                # 5.and/or
                    # and条件相连 有一列有索引都会命中
                    # or条件相连 所有列都有索引才能命中
                # 6.联合索引 *****
                    # create index mix_ind on 表 (id,name,email)
                    # 遵循最左前缀原则,且从出现范围开始索引失效
                    # select * from 表 where id = 123; 命中索引
                    # select * from 表 where id > 123; 不命中索引
                    # select * from 表 where id = 123 and name = 'alex'; 命中索引
                    # select * from 表 where id > 123 and name = 'alex'; 不命中索引
                    # select * from 表 where id = 123 and email = 'alex@oldboy'; 命中索引
                    # select * from 表 where email = 'alex@oldboy'; 不命中索引,因为条件中没有id
                    # select * from 表 where name='alex' and email = 'alex@oldboy'; 不命中索引,因为条件中没有id
                # 7.条件中的数据类型和实际字段的类型必须一致
                # 8.select字段中应该包含order by 中的字段
                    # select age from 表 order by age;   快
                    # select name from 表 order by age;  慢

# 覆盖索引 : 查询过程中不需要回表
#  select id from 表  where id > 10000000;
#  select max(id) from 表  where id > 10000000;
#  select count(id) from 表  where id > 10000000;

# 索引合并 : 分别创建的两个索引在某一次查询中临时合并成一条索引  a=1 or b=2
# 执行计划 : explain select 语句 ;能够查看sql语句有没有按照预期执行,可以查看索引的使用情况,type等级
# 慢查询优化 :
    # 首先从sql的角度优化
        # 把每一句话单独执行,找到效率低的表,优化这句sql
        # 了解业务场景,适当创建索引,帮助查询
        # 尽量用连表代替子查询
        # 确认命中索引的情况
    # 考虑修改表结构
        # 拆表
        # 把固定的字段往前调整
    # 使用执行计划,观察sql的type通过以上调整是否提高
# mysql的慢日志
    # 在mysql的配置中开启并设置一下
    # 在超过设定时间之后,这条sql总是会被记录下来,
    # 这个时候我们可以对这些被记录的sql进行定期优化

