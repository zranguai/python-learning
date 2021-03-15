import socket
import hashlib

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))

secret_id = b'hahaha'

rand = sk.recv(32)
sha = hashlib.sha1(secret_id)
sha.update(rand)
rres = sha.hexdigest()

sk.send(rres.encode('utf-8'))

msg = sk.recv(1024)
print(msg)
sk.close()










