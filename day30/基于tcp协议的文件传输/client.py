import socket
import os
import json
import struct
# 发送
sk = socket.socket()
sk.connect(('127.0.0.1', 9001))



# 文件名/文件大小
abs_path = r"D:\老男孩python22期代码及笔记\day30\temp.txt"
filename = os.path.basename(abs_path)
filesize = os.path.getsize(abs_path)

dic = {'filename': filename, 'filesize': filesize}
str_dic = json.dumps(dic)
b_dic = str_dic.encode('utf-8')
mlen = struct.pack('i', len(b_dic))

sk.send(mlen) # 四个字节 表示字典转换成字节之后的 长度
sk.send(b_dic) # 具体的字典数据
# sk.send(str_dic.encode('utf-8'))  # 可能会发生粘包


# 发送小文件
# with open(abs_path,mode='rb') as f:
#     content = f.read()
#     sk.send(content)

# 发送大文件
with open(abs_path,mode='rb') as f:
    while filesize > 0:
        content = f.read(1024)
        filesize -= len(content)
        sk.send(content)
sk.close()
