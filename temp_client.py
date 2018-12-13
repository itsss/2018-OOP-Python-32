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

cnt_now=1

#서버로부터 데이터를 받는 함수
#start를 전송받으면 게임을 시작 / 함수를 종료
def ready():
    while True and cnt_now:
        try:
            data=mysock.recv(1024)
        except OSError:
            break
        print(data.decode('utf-8'))
        if data.decode('utf-8')=="start":
            break

#입력받아 서버에 전송하는 함수 / 채팅함수
def client_chat(mysocket):
    #스레드로 데이터 받는 함수 실행
    Re=threading.Thread(target=ready, args=())
    Re.start()
    #스레드 탈출 변수
    # exit를 입력하면 탈출
    while cnt_now:
        try:
            w=input()
            if w=='exit':
                break
        except KeyboardInterrupt:
            print("Error!")
            break
        except OSError:
            print("Error!")
            break
        mysocket.send(w.encode('utf-8'))

    mysock.close()
    print("You get out from server.")


client_chat(mysock)
