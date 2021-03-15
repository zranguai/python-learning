import socket
sk = socket.socket()

sk.connect(('127.0.0.1', 9001))

username = input('请输入用户名')
sk.send(username.encode('utf-8'))
password = input('请输入密码')
sk.send(password.encode('utf-8'))

msg = sk.recv(1024).decode('utf-8')
print(msg, type(msg))
if msg == 'success':
    print('登入成功')
else:
    print('登入失败')
sk.close()