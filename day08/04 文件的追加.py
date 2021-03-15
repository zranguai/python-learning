# mode= a,ab,a+,a+b
# 没有文件，创建文件，追加文件(没打开文件时，光标再开始位置，只要一追加就把光标调到最后，在读后光标就在后面了)
# f = open('文件的追加', mode='a', encoding='utf-8')
# f.write('123haha呵呵')
# f.close()

# 有文件，追加
f = open('文件的追加', mode='a', encoding='utf-8')
f.write('ooo哦哦哦哦哦')
f.close()
