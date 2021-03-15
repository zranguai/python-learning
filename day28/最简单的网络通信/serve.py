# 基于tcp协议
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

conn, addr = sk.accept()
conn.send(b'hell')
msg = conn.recv(1024)    # 最多接受1024个字节
print(msg)

conn.close()    # 断开连接

sk.close()    # 关闭整个serve服务





















