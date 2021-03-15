f1 = open('d:\python文件操作初始.txt', mode='r', encoding='utf-8')
content = f1.read()
print(content)
f1.close()
'''
open 内置函数，底层调用的是操作系统的接口
f1 文件句柄，对文件的任何操作都要通过文件局部.方式
encoding: 可以不写，默认是操作系统的默认编码
f1.close() 关闭文件句柄，要是不关会一直占用内存
'''
'''
文件操作三部曲：
1.打开文件
2.对文件句柄进行相应的操作
3.关闭文件
'''