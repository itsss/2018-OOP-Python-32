#임시 클라이언트
import socket
import threading

# 접속하고자 하는 서버의 주소 및 포트
server_ip = '127.0.0.1'
server_port = 60000
address = (server_ip, server_port)

# socket을 이용해서 접속 할 준비
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(address)  # 서버에 접속

#입력받아 서버에 전송하는 함수 / 채팅함수
#에러 코드
#exit를 입력하면 정상적으로 스레딩이 종료되야 함. 현재는 스크롤이 무한히 내려가는 중
def chat(mysocket):
    while True:
        try:
            w=input()
            mysocket.send(w.encode('utf-8'))
            if w=='exit':
                break
        except OSError:
            print("Error!")
            mysocket.close()
            break

def ready():
    Ch=threading.Thread(target=chat, args=(mysock,))
    Ch.start()
    while True:
        try:
            data=mysock.recv(1024)
        except OSError:
            break
        print(data.decode('utf-8'))
        if data.decode('utf-8')=="start":
            break

ready()
now=input()
mysock.send(now.encode('utf-8'))
