import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

conn, addr = sk.accept()

username = conn.recv(1024).decode('utf-8')
print(username, type(username))
password = conn.recv(1024).decode('utf-8')
print(password, type(password))

if username == 'xiaoming' or password == '123':
    conn.send('success'.encode('utf-8'))
else:
    conn.send('failure'.encode('utf-8'))

conn.close()

sk.close()