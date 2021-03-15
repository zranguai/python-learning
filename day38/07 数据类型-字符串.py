# char
# varchar

# char(18)    # 最多只能表示255个字符
#     定长存储，浪费空间，节省时间
#     'alex'    'alex           '
# varchar(18) # 最多能表示65535个字符
#     变长存储，更节省空间,存取速度慢
#     'alex'     'alex4'


# 适合使用char
#     身份证号
#     手机号码
#     qq号
#     username 12-18
#     password 10-16
#     银行卡号
#
# 适合使用varchar
#     评论
#     朋友圈
#     微博


# 建表
# create table t6(
#     c1 char,
#     v1 varchar(1),    # 必须写长度
#     c2 char(8),
#     v2 varchar(8)
# );




