# 读写mode='r+'： 先读后写(本质：读并追加)/顺序不能错
f = open('文件的读写', mode='r+', encoding='utf-8')
content = f.read()
print(content)
f.write('人的一切痛苦，本质都是对自己无能的愤怒')
f.close()
