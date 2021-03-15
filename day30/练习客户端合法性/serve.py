import socket
import os
import hashlib

sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

secret_id = b'hahaha'

conn, addr = sk.accept()
res1 = os.urandom(32)
conn.send(res1)

sha = hashlib.sha1(secret_id)
sha.update(res1)
current_rres = sha.hexdigest()

res = conn.recv(1024).decode('utf-8')

if res == current_rres:
    print('登入成狗')
    conn.send(b'success')
else:
    print('登入失败')
    conn.close()
sk.close()


