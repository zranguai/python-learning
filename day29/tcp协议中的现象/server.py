import socket
import struct
sk = socket.socket()
sk.bind(('127.0.0.1', 9001))# 申请操作系统的资源
sk.listen()

conn, addr = sk.accept()# conn里存储的是一个客户端和我serve端的连接信息

msg1 = input('>>>').encode()
msg2 = input('>>>').encode()
# num = str(len(msg1))  # '6'
# ret = num.zfill(4)    #  '0006'
# conn.send(ret.encode('utf-8'))
blen = struct.pack('i', len(msg1))
print(blen)
conn.send(blen)
conn.send(msg1)
conn.send(msg2)


conn.close()    # 四次挥手,断开连接

sk.close()    # 关闭服务，归还申请的操作系统资源
