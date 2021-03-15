import socket
import os
import hashlib

secret_key = b'hahaha'
sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

conn, addr = sk.accept()
# 创建一个随机的字符串
rand = os.urandom(32)
# 发送随机字符串
conn.send(rand)

# 根据发送的字符串 + secrete key 进行摘要

sha = hashlib.sha1(secret_key)
sha.update(rand)
res = sha.hexdigest()

# 等待接受客户端的摘要结果
res_client = conn.recv(1024).decode('utf-8')
# 做对比
if res_client == res:
    print('是合法的客户端')
    conn.send(b'hello')
else:
    conn.close()
    # 如果不一致，这关闭连接






