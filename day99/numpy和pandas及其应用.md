# numpy和pandas的学习及应用
## Numpy(Numerical Python)
+ 简介: NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。
### 创建ndarray
#### 使用np.array()创建
1. 一维数组创建
```python
import numpy as np
np.array([1,2,3,4,5])
```
2. 二维数组创建
```python
np.array([[1,1.2,3],[4,5,'six']) 
```
+ 注意：
  - numpy默认ndarray的所有元素的类型是相同的
  - 如果传进来的列表中包含不同的类型，则统一为同一类型，优先级：str>float>int
+ 案例:使用matplotlib.pyplot获取一个numpy数组，数据来源于一张图片
```python
import matplotlib.pyplot as plt
img_arr = plt.imread('./cat.jpg')
print(plt.imshow(img_arr))
plt.imshow(img_arr - 150)    # 变化后的图像
```
#### 使用np的routines函数创建
```python
1. np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None) # 等差数列
np.linspace(1,100,num=10) # 成等差数列分成10份

 2. np.arange([start, ]stop, [step, ]dtype=None)
np.arange(0,100,2) # 每个数字之间间隔为2

3. np.random.randint(low, high=None, size=None, dtype='l')
# - 随机原理
#    - 随机因子：表示的是一个无时无刻都在变化的数值
np.random.seed(10) # 里面值是随机因子，当里面的值固定的化参数的数字不会变了
np.random.randint(0,100,size=(4,5)) # 生成4行5列的二维数组

4. np.random.random(size=None)  
# 生成0到1的随机数，左闭右开         np.random.seed(3)
np.random.random(size=(5,3)) # 生成5行3列的数组，元素范围为0到1
```
### ndarray的属性
+ 4个必记参数
```text
ndim：维度
shape：形状（各维度的长度）
size：总长度
dtype：元素类型
```
+ 其他
```text
img_arr.ndim    # 维度
img_arr.shape   # 返回的形状
img_arr.size    # 总长度
img_arr.dtype

type(img_arr)
```
### ndarray的基本操作
1. 索引
+ 一维与列表完全一致 多维时同理
```python
arr = np.random.randint(60,120,size=(6,8)) # 随机生成60到120的整数，矩阵的大小为6*8
print(arr)

# 根据索引修改数据
arr[1]    # 取第一行的数据
arr[1][2]
```
2. 切片
+ 一维与列表完全一致 多维时同理
```python
arr同上
# 获取二维数组前两行
arr[0:2]

# 获取二维数组前两列
arr[:,0:2] # 应用了逗号的机制，逗号左边为第一个维度行，右边为第二个维度列

# 将数据反转，例如[1,2,3]---->[3,2,1]
# ::进行切片

#将数组的行倒序
arr[::-1]

#列倒序
arr[:,::-1]

#全部倒序
arr[::-1,::-1]
```
3. 变形
+ 使用arr.reshape()函数，注意参数是一个tuple！
- 基本使用
1. 将一维数组变形成多维数组
```python
print(arr.shape) # 返回的形状
arr.reshape((24, 2)) # 里面元素的个数应该一致，否则会报错
arr.reshape((-1,4)) # 为4列，行自动补齐
```
4. 级联
级联需要注意的点：
- 级联的参数是列表：一定要加中括号或小括号
- 维度必须相同
- 形状相符:在维度保持一致的前提下，如果进行横向（axis=1）级联，必须保证进行级联的数组行数保持一致。如果进行纵向（axis=0）级联，必须保证进行级联的数组列数保持一致。
- 可通过axis参数改变级联的方向
```
axis=1横向
+++++++++++
+   +     +
+++++++++++
axis=0纵向
+++++++
+     +
+++++++
+     +
+++++++
```
    np.concatenate()
```python
# 1.一维，二维，多维数组的级联，实际操作中级联多为二维数组
np.concatenate((arr,arr),axis=1)     # axis=0列 axis=1行

   理解axis:https://i.stack.imgur.com/h1alT.jpg
# 2.合并两张照片
arr_3 = np.concatenate((img_arr,img_arr,img_arr),axis=1)
arr_9 = np.concatenate((arr_3,arr_3,arr_3),axis=0)
plt.imshow(arr_9)
```
+ arr_3时
![](https://img-blog.csdnimg.cn/20210114215919913.png)
+ arr_9时
![](https://img-blog.csdnimg.cn/20210114215948687.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTAzNjk0NA==,size_16,color_FFFFFF,t_70)
+ axis轴向问题
![](https://img-blog.csdnimg.cn/20210114215856544.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTAzNjk0NA==,size_16,color_FFFFFF,t_70)
### ndarray的聚合操作
1. 求和np.sum
```
arr.sum(axis=1)    # axis=0每一列的和axis=1求每一行的和
```
2. 最大最小值：np.max/ np.min
3. 平均值：np.mean()
4. 其他聚合操作
```
Function Name    NaN-safe Version    Description
np.sum    np.nansum    Compute sum of elements
np.prod    np.nanprod    Compute product of elements
np.mean    np.nanmean    Compute mean of elements
np.std    np.nanstd    Compute standard deviation
np.var    np.nanvar    Compute variance
np.min    np.nanmin    Find minimum value
np.max    np.nanmax    Find maximum value
np.argmin    np.nanargmin    Find index of minimum value
np.argmax    np.nanargmax    Find index of maximum value
np.median    np.nanmedian    Compute median of elements
np.percentile    np.nanpercentile    Compute rank-based statistics of elements
np.any    N/A    Evaluate whether any elements are true
np.all    N/A    Evaluate whether all elements are true
np.power 幂运算
```
### ndarray的排序
1. 快速排序
```
np.sort()与ndarray.sort()都可以，但有区别：
- np.sort()不改变输入
- ndarray.sort()本地处理，不占用空间，但改变输入

arr.sort(axis=1) 
print(arr)
# 裁剪
plt.imshow(img_arr)
plt.imshow(img_arr[50:400,100:330,:])
```
## Pandas
### 导入pandas：
```python
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
```
#### Series
1. Series的创建
+ 由列表或numpy数组创建,默认索引为0到N-1的整数型索引
```python
1. #使用列表创建Series
Series(data=[1,2,3,4,5])    # 只能是一维数组
2. # 使用numpy数组创建
Series(data=np.random.randint(0,100,size=(10,)))
3. 还可以通过设置index参数指定索引
Series(data=[1,2,3],index=['a','b','c']) #显式索引
```
2. Series的索引和切片
+ 可以使用中括号取单个索引（此时返回的是元素类型），或者中括号里<font color=red>一个列表</font>取多个索引（此时返回的是一个Series类型）。
+ (1) 显式索引
```
 - 使用index中的元素作为索引值
    - 使用s.loc[]（推荐）:注意，loc中括号中放置的一定是显示索引
 注意，此时是闭区间
s = Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s)
print(s[1])
print(s['a'])
print(s.a)   # 只能是显示索引可以点出来
```
+ (2) 隐式索引：一般是整数
```
    - 使用整数作为索引值
    - 使用.iloc[]（推荐）:iloc中的中括号中必须放置隐式索引
注意，此时是半开区间
s[1:3]
# s['a':'d']
```
3. Series的基本概念
```
可以使用s.head(),tail()分别查看前n个和后n个值
s.head(3)
对Series元素进行去重
s = Series([1,1,2,2,3,4,5,56,6,7,78,8,89])
s.unique()
当索引没有对应的值时，可能出现缺失数据显示NaN（not a number）的情况
使得两个Series进行相加
s1 = Series([1,2,3],index=['a','b','c'])
s2 = Series([1,2,3],index=['a','d','c'])
s = s1 + s2    # 索引对齐的进行算术算法
print(s)

a    2.0
b    NaN
c    6.0
d    NaN
dtype: float64

可以使用pd.isnull()，pd.notnull()，或s.isnull(),notnull()函数检测缺失数据
# 取值
s[[1,2]]
s[['a','b']]
s[[True,False,True,False]]

a    2.0
b    NaN
c    6.0
dtype: float64

s.isnull()
a    False
b     True
c    False
d     True
dtype: bool
s.notnull()
a     True
b    False
c     True
d    False
dtype: bool
s[s.notnull()]
a    2.0
c    6.0
dtype: float64
Series之间的运算
- 在运算中自动对齐不同索引的数据
- 如果索引不对应，则补NaN
```
#### DataFrame == mysql的table
+ DataFrame是一个【表格型】的数据结构。DataFrame由按一定顺序排列的多列数据组成。设计初衷是将Series的使用场景从一维拓展到多维。DataFrame既有行索引，也有列索引。
- 行索引：index
- 列索引：columns
- 值：values
1. DataFrame的创建
+ 最常用的方法是传递一个字典来创建。DataFrame以字典的键作为每一【列】的名称，以字典的值（一个数组）作为每一列。
+ 此外，DataFrame会自动加上每一行的索引。
+ 使用字典创建的DataFrame后，则columns参数将不可被使用。
+ 同Series一样，若传入的列与字典的键不匹配，则相应的值为NaN。
###
+ 使用ndarray创建DataFrame
```
df = DataFrame(data=np.random.randint(0,100,size=(3,4)),index=['a','b','c'],columns=['A','B','C','D'])
print(df)
```
+ DataFrame属性：values、columns、index、shape
```
df.values    # 值
df.columns    # 列索引
df.index      # 行索引
df.shape    # 形状
```
+ 案例
```python
# 使用ndarray创建DataFrame：创建一个表格用于展示张三，李四的成绩
dic = {
    '张三':[150,150,150,150],    # 字典的key作为列
    '李四':[0,0,0,0]
}
df = DataFrame(data=dic,index=['语文','数学','英语','理综'])    # columns参数将不可被使用
print(df)
```
#### 索引
+ DataFrame的索引,,,,对列索引直接拿，对行索引使用loc/iloc
1. 对列进行索引
    - 通过类似字典的方式  df['q']
    - 通过属性的方式     df.q
+ 可以将DataFrame的列获取为一个Series。返回的Series拥有原DataFrame相同的索引，且name属性也已经设置好了，就是相应的列名。
df
```
#修改列索引
df['张三']
#获取前两列
df[['李四','张三']]
```
2. 对行进行索引
   - 使用列索引
   - 使用行索引(iloc[3,1] or loc['C','q']) 行索引在前，列索引在后
```
同样返回一个Series，index为原来的columns。
df.loc['语文']    # 显示索引
df.iloc[0]    # 用作行的提取，隐式索引
df.iloc[[0,1]]
```
3. 对元素索引的方法
- 使用列索引
- 使用行索引(iloc[3,1] or loc['C','q']) 行索引在前，列索引在后
```python
df
df['张三']['英语']    # 使用列索引，列在前
df.loc['英语','张三']    # 使用行索引，有逗号，左边是行，右边是列，行在前
df.loc[['数学','理综'],'张三']
```
#### 切片  对行切片直接拿，对列切片使用loc/iloc
【注意】
直接用中括号时：
- 索引表示的是列索引
- 切片表示的是行切片
```
df
df[0:2]    # 切行不需要夹loc或iloc，
在loc和iloc中使用切片(切列) ： df.loc['B':'C','丙':'丁']
df.iloc[:,0:1]    # 切列需要夹loc或iloc
```
```
- 索引
    - df[列索引]：取一列
    - df[[col1,col2]]:取出两列
    - df.loc[显示的行索引]：取行
    - df.loc[行,列]：取元素
- 切片：
    - df[index1:index3]:切行
    - df.loc[col1:col3]:切列
```
#### DataFrame的运算
+ 同Series一样：
  - 在运算中自动对齐不同索引的数据
  - 如果索引不对应，则补NaN
## 应用
### 删除/覆盖
1. 删除
+ 固定搭配：
    + isnull-->any
    + notnull-->all
+ 判断函数
    + isnull()
    + notnull()

+ df.dropna()可以选择过滤的是行还是列(默认为行):axis中0表示行1表示列
+ df.dropna(axis=0)
2. 覆盖
可以选择是向前覆盖（method='ffill'）还是向后覆盖(method='bfill')
+ df.fillna(method='bfill', axis=0)    # axis=0是列
### pandas的拼接操作
+ pandas的拼接分为两种：
  - 级联：pd.concat, pd.append
  - 合并：pd.merge, pd.join
#### 使用pd.concat()级联
pandas使用pd.concat函数，与np.concatenate函数类似，只是多了一些参数：
```
objs
axis=0
keys
join='outer' / 'inner':表示的是级联的方式，outer会将所有的项进行级联（忽略匹配和不匹配），而inner只会将匹配的项级联到一起，不匹配的不级联
ignore_index=False
```
#####  1)匹配级联
```python
import pandas as pd
from pandas import Series,DataFrame
import numpy as np

df1 = DataFrame(data=np.random.randint(0,100,size=(3,4)),index=['a','b','c'])
df2 = DataFrame(data=np.random.randint(0,100,size=(3,3)),index=['a','d','c'])

pd.concat((df1,df1),axis=0)    # 0是行
```
##### 2)不匹配级联
```text
不匹配指的是级联的维度的索引不一致。例如纵向级联时列索引不一致，横向级联时行索引不一致
有2种连接方式：
- 外连接：补NaN（默认模式）
- 内连接：只连接匹配的项
pd.concat((df1,df2),axis=0,join='inner')    # join='inner'只连接匹配的项有nan就删除
```
#### 使用pd.merge()合并
merge与concat的区别在于，merge需要依据某一共同的列来进行合并

使用pd.merge()合并时，会自动根据两者相同column名称的那一列，作为key来进行合并。

注意每一列元素的顺序不要求一致

参数：
- how：out取并集   inner取交集
- on：当有多列相同的时候，可以使用on来指定使用那一列进行合并，on的值为一个列表
#####  1) 一对一合并
```python
df1 = DataFrame({'employee':['Bob','Jake','Lisa'],
                'group':['Accounting','Engineering','Engineering'],
                })
df1

df2 = DataFrame({'employee':['Lisa','Bob','Jake'],
                'hire_date':[2004,2008,2012],
                })
df2

pd.merge(df1,df2,on='employee')    # 不写默认是连表相同的
```
##### 2) 多对一合并
```python
df3 = DataFrame({
    'employee':['Lisa','Jake'],
    'group':['Accounting','Engineering'],
    'hire_date':[2004,2016]})
df3


df4 = DataFrame({'group':['Accounting','Engineering','Engineering'],
                       'supervisor':['Carly','Guido','Steve']
                })
df4
```
##### 3) 多对多合并
```python
df1 = DataFrame({'employee':['Bob','Jake','Lisa'],
                 'group':['Accounting','Engineering','Engineering']})
df1

df5 = DataFrame({'group':['Engineering','Engineering','HR'],
                'supervisor':['Carly','Guido','Steve']
                })
df5

pd.merge(df1,df5,how='outer')    # how合并的方式，out保证数据不丢失，能合并的合并不能合并的补充0
```
##### 4) key的规范化
- 当列冲突时，即有多个列名称相同时，需要使用on=来指定哪一个列作为key，配合suffixes指定冲突列名
```python
df1 = DataFrame({'employee':['Jack',"Summer","Steve"],
                 'group':['Accounting','Finance','Marketing']})
df1

df2 = DataFrame({'employee':['Jack','Bob',"Jake"],
                 'hire_date':[2003,2009,2012],
                'group':['Accounting','sell','ceo']})
df2

pd.merge(df1,df2,on='group',how='outer')
```
- 当两张表没有可进行连接的列时，可使用left_on和right_on手动指定merge中左右两边的哪一列列作为连接的列
```python
df1 = DataFrame({'employee':['Bobs','Linda','Bill'],
                'group':['Accounting','Product','Marketing'],
               'hire_date':[1998,2017,2018]})
df1

df5 = DataFrame({'name':['Lisa','Bobs','Bill'],
                'hire_dates':[1998,2016,2007]})

df5

pd.merge(df1,df5,left_on='employee',right_on='name',how='outer')
```
#####  5) 内合并与外合并:out取并集   inner取交集
- 内合并：只保留两者都有的key（默认模式）
```python
df6 = DataFrame({'name':['Peter','Paul','Mary'],
               'food':['fish','beans','bread']}
               )
df7 = DataFrame({'name':['Mary','Joseph'],
                'drink':['wine','beer']})
```               
# pandas数据处理
## 1、删除重复元素
使用duplicated()函数检测重复的行，返回元素为布尔类型的Series对象，每个元素对应一行，如果该行不是第一次出现，则元素为True

- keep参数：指定保留哪一重复的行数据
- 创建具有重复元素行的DataFrame
```
import pandas as pd
from pandas import Series,DataFrame
import numpy as np

#创建一个df
df = DataFrame(data=np.random.randint(0,100,size=(10,6)))
df

#手动将df的某几行设置成相同的内容(为了测试后面的删除重复行)
df.iloc[1] = [1,1,1,1,1,1]
df.iloc[3] = [1,1,1,1,1,1]
df.iloc[7] = [1,1,1,1,1,1]

df
```
- 使用drop_duplicates()函数删除重复的行
    - drop_duplicates(keep='first/last'/False)
df.drop_duplicates(keep='first')    # 再重复中保留第一个出现的删除后面出现的
## 2. 映射
### 1) replace()函数：替换元素
使用replace()函数，对values进行映射操作
#### DataFrame替换操作
- 单值替换
    - 普通替换：  替换所有符合要求的元素:to_replace=15,value='e'
    - 按列指定单值替换： to_replace={列标签：替换值} value='value'       
- 多值替换
    - 列表替换: to_replace=[]  value=[]
    - 字典替换（推荐）  to_replace={to_replace:value,to_replace:value}
df.replace(to_replace=4,value='four')
df.replace(to_replace=1,value='one')

df.replace(to_replace={3:1},value='one')
注意：DataFrame中，无法使用method和limit参数

#### 2) map()函数：新建一列 ，   map函数并不是df的方法，而是series的方法
- map()可以映射新一列数据
- map()中可以使用lambd表达式
- map()中可以使用方法，可以是自定义的方法

    eg:map({to_replace:value})
- **注意** map()中不能使用sum之类的函数，for循环

#### map当作映射
```
新增一列：给df中，添加一列，该列的值为中文名对应的英文名
dic = {
    'name':['周杰伦','张三','周杰伦'],
    'salary':[20000,12000,20000]
}
df = DataFrame(data=dic)
df
```
#### 映射关系表
```
dic = {
    '周杰伦':'jay',
    '张三':'tom'
}
df['e_name'] = df['name'].map(dic)
df
##################
name	salary	e_name
0	周杰伦	20000	jay
1	张三	12000	tom
2	周杰伦	20000	jay
###################
```
##### map当做一种运算工具，至于执行何种运算，是由map函数的参数决定的（参数：lambda，函数）
- 使用自定义函数
- map既可作运算工具又可以做映射
def after_sal(s):    # 要传s
    return s - (s-3000)*0.5

#### 超过3000部分的钱缴纳50%的税
```
df['after_sal'] = df['salary'].map(after_sal)
df
```
#### 超过3000部分的钱缴纳50%的税
```
df['after_sal'] = df['salary'].map(after_sal)
df
###################
name	salary	e_name	after_sal
0	周杰伦	20000	jay	11500.0
1	张三	12000	tom	7500.0
2	周杰伦	20000	jay	11500.0
############################
```
df['salary'].apply(after_sal)    # 与map运算类似但是比map运算更快
+ apply和map都可以作为一种基于Series的运算工具，并且apply比map更快
##### 注意：并不是任何形式的函数都可以作为map的参数。只有当一个函数具有一个参数且有返回值，那么该函数才可以作为map的参数。

## 3. 使用聚合操作对数据异常值检测和过滤
使用df.std()函数可以求得DataFrame对象每一列的标准差
df = DataFrame(data=np.random.random(size=(1000,3)),columns=['A','B','C'])
df
对df应用筛选条件,去除标准差太大的数据:假设过滤条件为 C列数据大于两倍的C列标准差
std_twice = df['C'].std() * 2

df['C'] > std_twice
df.loc[df['C'] > std_twice]
indexs = df.loc[df['C'] > std_twice].index
indexs
df.drop(labels=indexs,axis=0,inplace=True)
df

### 数据清洗
- 清洗空值
    - df.dropna()
    - df.fillna()
- 清洗重复值
    - df.drop_duplicates()
- 清洗异常值
    - 异常值判定的条件
    - 异常值对应的行数据进行删除 

## 4. 排序
#### 使用.take()函数排序
    - take()函数接受一个索引列表，用数字表示,使得df根据列表中索引的顺序进行排序
    - eg:df.take([1,3,4,2,5])
可以借助np.random.permutation()函数随机排序

可以借助np.random.permutation()函数随机排序
np.random.permutation(3)

df.take(np.random.permutation(3),axis=1).take(np.random.permutation(100),axis=0)[0:10]

np.random.permutation(x)可以生成x个从0-(x-1)的随机数列
#### 随机抽样
当DataFrame规模足够大时，直接使用np.random.permutation(x)函数，就配合take()函数实现随机抽样

## 5. 数据分类处理【重点】
数据聚合是数据处理的最后一步，通常是要使每一个数组生成一个单一的数值。

数据分类处理：

 - 分组：先把数据分为几组
 - 用函数处理：为不同组的数据应用不同的函数以转换数据
 - 合并：把不同组得到的结果合并起来
 
数据分类处理的核心：
     - groupby()函数
     - groups属性查看分组情况
     - eg: df.groupby(by='item').groups
```
from pandas import DataFrame,Series
df = DataFrame({'item':['Apple','Banana','Orange','Banana','Orange','Apple'],
                'price':[4,3,3,2.5,4,2],
               'color':['red','yellow','yellow','green','green','green'],
               'weight':[12,20,50,30,20,44]})
df
df.groupby(by='item',axis=0)
使用groups查看分组情况

#该函数可以进行数据的分组，但是不显示分组情况
df.groupby(by='item',axis=0).groups
#给df创建一个新列，内容为各个水果的平均价格
df.groupby(by='item',axis=0).mean()['price']
s = df.groupby(by='item',axis=0)['price'].mean()
s.to_dict()
df['item'].map(s.to_dict())    # 做映射(转换成字典)

df['mean_price'] = df['item'].map(s.to_dict())
df
```
## 6.0 高级数据聚合
#### 使用groupby分组后，也可以使用transform和apply提供自定义函数实现更多的运算

 - df.groupby('item')['price'].sum() <==> df.groupby('item')['price'].apply(sum)
 - transform和apply都会进行运算，在transform或者apply中传入函数即可
 - transform和apply也可以传入一个lambda表达式
```
def myMean(s):#必须要有一个参数
    sum = 0
    for i in s:
        sum += i
    return sum/len(s)
```
+ df.groupby(by='item')['price'].apply(myMean)#apply返回值是没有经过映射的
```
#################
item
Apple     3.00
Banana    2.75
Orange    3.50
Name: price, dtype: float64
##################
```
+ df.groupby(by='item')['price'].transform(myMean) #transform返回值是经过映射的
```
###################
0    3.00
1    2.75
2    3.50
3    2.75
4    3.50
5    3.00
Name: price, dtype: float64
###################
```
# 案例:线性回归算法--城市气候与海洋的关系研究
导入模块
```
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
```

### 防止加中文出现乱码
```
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
导入数据各个海滨城市数据
ferrara1 = pd.read_csv('./ferrara_150715.csv')
ferrara2 = pd.read_csv('./ferrara_250715.csv')
ferrara3 = pd.read_csv('./ferrara_270615.csv')
ferrara=pd.concat([ferrara1,ferrara1,ferrara1],ignore_index=True)

torino1 = pd.read_csv('./torino_150715.csv')
torino2 = pd.read_csv('./torino_250715.csv')
torino3 = pd.read_csv('./torino_270615.csv')
torino = pd.concat([torino1,torino2,torino3],ignore_index=True) 

mantova1 = pd.read_csv('./mantova_150715.csv')
mantova2 = pd.read_csv('./mantova_250715.csv')
mantova3 = pd.read_csv('./mantova_270615.csv')
mantova = pd.concat([mantova1,mantova2,mantova3],ignore_index=True) 

milano1 = pd.read_csv('./milano_150715.csv')
milano2 = pd.read_csv('./milano_250715.csv')
milano3 = pd.read_csv('./milano_270615.csv')
milano = pd.concat([milano1,milano2,milano3],ignore_index=True) 

ravenna1 = pd.read_csv('./ravenna_150715.csv')
ravenna2 = pd.read_csv('./ravenna_250715.csv')
ravenna3 = pd.read_csv('./ravenna_270615.csv')
ravenna = pd.concat([ravenna1,ravenna2,ravenna3],ignore_index=True)

asti1 = pd.read_csv('./asti_150715.csv')
asti2 = pd.read_csv('./asti_250715.csv')
asti3 = pd.read_csv('./asti_270615.csv')
asti = pd.concat([asti1,asti2,asti3],ignore_index=True)

bologna1 = pd.read_csv('./bologna_150715.csv')
bologna2 = pd.read_csv('./bologna_250715.csv')
bologna3 = pd.read_csv('./bologna_270615.csv')
bologna = pd.concat([bologna1,bologna2,bologna3],ignore_index=True)

piacenza1 = pd.read_csv('./piacenza_150715.csv')
piacenza2 = pd.read_csv('./piacenza_250715.csv')
piacenza3 = pd.read_csv('./piacenza_270615.csv')
piacenza = pd.concat([piacenza1,piacenza2,piacenza3],ignore_index=True)

cesena1 = pd.read_csv('./cesena_150715.csv')
cesena2 = pd.read_csv('./cesena_250715.csv')
cesena3 = pd.read_csv('./cesena_270615.csv')
cesena = pd.concat([cesena1,cesena2,cesena3],ignore_index=True)

faenza1 = pd.read_csv('./faenza_150715.csv')
faenza2 = pd.read_csv('./faenza_250715.csv')
faenza3 = pd.read_csv('./faenza_270615.csv')
faenza = pd.concat([faenza1,faenza2,faenza3],ignore_index=True)
```
+ 去除没用的列
```
city_list = [ferrara,torino,mantova,milano,ravenna,asti,bologna,piacenza,cesena,faenza]
for city in city_list:
    city.drop(labels='Unnamed: 0',axis=1,inplace=True)
```
+ 显示最高温度于离海远近的关系（观察多个城市）
```
max_temp = []
city_dist = []
for city in city_list:
    temp = city['temp'].max()
    max_temp.append(temp)
    dist = city['dist'].max()
    city_dist.append(dist)

city_dist
```
### 画散点图--判断是否为线性关系
```
plt.scatter(city_dist,max_temp)
plt.xlabel('距离')
plt.ylabel('温度')
plt.title('海滨城市最高温度和离还远近之间的关系')
```
## 背景简介
- 需求：需要对当前的数据建立一个算法模型，然后可以让模型实现预测的功能（根据距离预测最高温度）。
    - y = wx + b线性方程，改方程还没有求出解
    - 如果方程中的w和b是已知的，则改方程就有解

- 人工智能和机器学习之间的关系是什么？
    - 机器学习是用来实现人工智能的一种技术手段
- 算法模型
    - 概念：特殊的对象。特殊之处就在于该对象内部已经集成或者封装好一个某种方程（还没有求出解的方程）
    - 作用：算法模型对象最终求出的解就是该算法模型实现预测或者分类的结果
        - 预测
        - 分类
- 样本数据：numpy，DataFrame
    - 样本数据和算法模型之间的关联：样本数据是需要带入到算法模型对象中对其内部封装的方程进行求解的操作。该过程被称为模型的训练。
    - 组成部分：
        - 特征数据：自变量（楼层，采光率，面积）
        - 目标数据：因变量（售价）
- 模型的分类：
    - 有监督学习：如果模型需要的样本数据中必须包含特征和目标数据，则该模型归为有监督学习的分类
    - 无监督学习：如果模型需要的样本数据只需要有特征数据即可。
    
- sklearn模块：大概封装了10多种算法模型对象。
    - 线性回归算法模型-》预测
    - KNN算法模型-》分类
                
### 导入sklearn，建立线性回归算法模型对象
```
from sklearn.linear_model import LinearRegression
linner = LinearRegression()
```
### 样本数据的封装/提取
```
feature = np.array(city_dist)
feature = feature.reshape(-1, 1)
target = np.array(max_temp)
```
### 对模型进行训练
    linner.fit(feature,target)  #X:二维形式的特征数据,y：目标数据

### 实现预测：对方程进行唯一值的求解
```
linner.predict(255)  #y = 3x + 5

linner.score(feature,target)
```
### 研究score的实现原理
```
print('模型预测的温度：',linner.predict(feature))
print('真实温度：',target)
```
### 回归的曲线画出
```
x = np.linspace(0,350,100).reshape(-1,1)
y = linner.predict(x)

plt.scatter(city_dist,max_temp)
plt.scatter(x,y)
plt.xlabel('距离')
plt.ylabel('温度')
plt.title('海滨城市最高温度和离还远近之间的关系')
```
