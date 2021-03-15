import socket
sk = socket.socket()
sk.connect(('127.0.0.1', 9001))

with open('a', mode='r', encoding='utf-8') as f1:
    mmsg = f1.read(1024)
    print(mmsg)
    sk.send(mmsg.encode('utf-8'))


msg = sk.recv(1024).decode('utf-8')
print(msg)
sk.close()















