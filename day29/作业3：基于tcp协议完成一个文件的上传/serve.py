import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

conn, addr = sk.accept()
with open('b', mode='w', encoding='utf-8') as f2:
    smsg = conn.recv(1024)
    f2.write(smsg.decode('utf-8'))


msg = '上传完成'
conn.send(msg.encode('utf-8'))

conn.close()
sk.close()
















