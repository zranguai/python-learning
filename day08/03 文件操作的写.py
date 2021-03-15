# 文件的写：w,wb,w+,w+b四种模式（前两种重要）

# 没有文件，创建文件写入内容
# f = open('文件的写', mode='w', encoding='utf-8')
# f.write('随便写一点')
# f.close()

# 如果文件存在，先清空原文件内容，再写入新的内容
# f = open('文件的写', mode='w', encoding='utf-8')
# f.write('哈哈很爱很爱你')
# f.close()

f = open('汽车.jpg', mode='rb')
content = f.read()
print(content)
f.close()

f1 = open('汽车2.jPg', mode='wb')
f1.write(content)
f1.close()