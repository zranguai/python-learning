import socket
import json
import struct
# 接受
sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

conn, addr = sk.accept()

msg_len = conn.recv(4)
dic_len = struct.unpack('i', msg_len)[0]
msg = conn.recv(dic_len).decode('utf-8')
msg = json.loads(msg)
# print(msg)
# 接受小文件
# with open(msg['filename'], mode='wb') as f:
    # content = conn.recv(msg['filesize'])
    # print('--->', len(content))
    # f.write(content)

# 接受大文件
with open(msg['filename'], 'wb') as f:
    while msg['filesize'] > 0:
        content = conn.recv(1024)
        msg['filesize'] -= len(content)# 他不写1024是因为可能发过来的不是1024
        f.write(content)
conn.close()
sk.close()
# 先登入
# 能选择上传/下载
# 作业1：实现文件下载
# 进阶：能上传到固定的目录/下载（从指定文件夹下选择文件）



