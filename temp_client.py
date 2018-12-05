#임시 클라이언트
import socket

# 접속하고자 하는 서버의 주소 및 포트
server_ip = '127.0.0.1'
server_port = 60000
address = (server_ip, server_port)

# socket을 이용해서 접속 할 준비
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)  # 서버에 접속

data = mysock.recv(1024)
print(data.decode('utf-8'))
now=input()
print(type(now))
mysock.send(now.encode('utf-8'))
