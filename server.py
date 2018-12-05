#초고 서버
import socket
import threading
import random

# 서버 주소, 포트
server_ip = '127.0.0.1'
server_port = 60000
address = (server_ip, server_port)

# 서버 연결 대기
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen()

#플레이어 목록, 최대 인원수
client_list=[]
client_score=[]
max_per=2

def connection():
    global client_list
    cnt=0
    while cnt<max_per:
        client_socket, client_address=server_socket.accept()
        #client=[client_socket, client_address]
        #client_list.append(client)
        client_list.append(client_socket)
        print("Connected from {}".format(client_address))
        print("Now players are")
        for i in client_list:
            print(str(client_list.index(i)+1)+". ", end="")
            print(i)
        cnt=cnt+1

def send_num(client_socket):
    num=random.randint(1,10)
    b_num=str(num).encode('utf-8')
    print(type(b_num))
    client_socket.send(b_num)

def receive(client_socket):
    try:
        data=client_socket.recv(1024)
        if data==(b"exit"):
            exit()
    except OSError:
        exit()
    print(data.decode('utf-8'))

connection()
print(1)
for i in client_list:
    send_num(i)
for i in client_list:
    B=threading.Thread(target=receive, args=(i,))
    B.start()
