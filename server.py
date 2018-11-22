# -*- coding: utf-8 -*-
"""
Title       OOP Project
Author      ITSC (Taewon Kang)
Date        2018.11.22
"""

import socket
import threading
# pip3 install -U beautifulsoup4
# pip3 install -U requests
import random
import requests  # 웹 접속 관련 라이브러리
from bs4 import BeautifulSoup as bs  # parsing library

# 서버의 설정값을 저장
myip = '127.0.0.1'
myport = 50035
address = (myip, myport)

# 서버 열기
sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.bind(address)
sck.listen()

print('Start economic - Server')

# 접속 클라이언트 저장 공간
client_list = []
client_id = []

# 서버로부터 메시지 수신
def receive(client_sock):
    global client_list  # 받은 메시지를 다른 클라이언트들에게 전송하고자 변수를 가져온다.
    while True:
        # 클라이언트로부터 데이터를 받는다.
        try:
            data = client_sock.recv(1024)
            # print('**' + data.decode('UTF-8'))
        except ConnectionError:
            print("{}와 연결이 끊겼습니다. #code1".format(client_sock.fileno()))
            break

        # 만약 클라이언트로부터 종료 요청이 온다면 종료한다.
        if not data:
            print("{}이 연결 종료 요청을 합니다. #code0".format(client_sock.fileno()))
            client_sock.send(bytes("서버에서 클라이언트 정보를 삭제하는 중입니다.", 'utf-8'))
            break

        if data.decode('UTF-8') == 'ex':
            data_send = 'Good!'
            # print(data_with_id)
            for sock in client_list:
                if sock == client_sock:  # == 자기 자신, != 자기 자신을 제외한 모두에게
                    sock.send(data_send)

    # 메시지 송발신이 끝났으므로, 대상인 client는 목록에서 삭제.
    client_id.remove(client_sock.fileno())
    client_list.remove(client_sock)
    print("현재 연결된 사용자: {}\n".format(client_id), end='')
    # 삭제 후 sock 닫기
    client_sock.close()
    print("클라이언트 소켓을 정상적으로 닫았습니다.")
    print('#----------------------------#')
    return 0


# 연결 수립용
def connection():
    global client_list
    global client_id

    while True:
        # 클라이언트들이 접속하기를 기다렸다가 연결을 수립함.
        client_sock, client_addr = sck.accept()

        # 연결된 정보를 가져와서 list에 저장함.
        client_list.append(client_sock)
        client_id.append(client_sock.fileno())

        print("{}가 접속하였습니다.".format(client_sock.fileno()))
        print("{}가 접속하였습니다.".format(client_addr))
        print("현재 연결된 사용자: {}\n".format(client_list))

        # 접속한 클라이언트를 기준으로 메시지를 수신 할 수 있는 스레드를 생성함.
        thread_recv = threading.Thread(target=receive, args=(client_sock,))
        thread_recv.start()


# 연결 수립용 스레드 생성 및 실행.
thread_server = threading.Thread(target=connection, args=())
thread_server.start()

print("============== AIPaper Server ==============")

thread_server.join()
sck.close()