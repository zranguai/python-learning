import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))

msg = sk.recv(1024)  # 最多接受1024个
print(msg)

sk.send(b'bebebe')

sk.close()