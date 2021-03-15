# 引擎介绍
# innodb
# myisam
# memory
# 表介绍
# 创建表
# 查看表结构

# mysql中的数据类型
# 数字  int unsigned, float
# 时间  date,time,datetime
# 字符串 char,varchar
# enum/set
# enum 单选行为
# set  对选行为

# 表的完整性约束
# 约束某一个字段
# 无符号的 int unsigned
# 不能为空 not null
# 默认值  default
# 唯一约束 unique
# 联合唯一 unique(字段1,字段2)
# 自增 auto_increment
# 只能对数字有效.自带非空约束
# 至少是unique的约束之后才能使用auto_increment
# 主键 primary key
# 一张表只能有一个
# 如果不指定主键,默认是第一个非空+唯一
# 联合主键 primary key(字段1,字段2)
# 外键 Foreign key
# Foreign key(自己的字段) references 外表(外表字段)
# 外表字段必须至少是"唯一"的

# 修改表结构



# 删除表       drop table 表名;
# 多表结构的创建与分析
