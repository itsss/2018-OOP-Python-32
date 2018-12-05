'''
게임 시작 전:
 - 사용자가 방에 입장하는 경우 모든 플레이어에게 (접속한 플레이어 모두) 접속자 명단을 보냄
 - 최대인원이 찬 경우 더 이상 입장할 수 없도록(?)
 - 최대인원이 차면 20초 내 게임을 시작함 (time:20 등과 같이 모든 플레이어에게 남은 시간 메시지를 보냄)

게임 시작 후:
 - 이후 입장하는 사용자는 방 입장을 제한함
 - 매 턴마다 사용자에게 입력을 받음. 사용자가 '결정' 버튼을 누르면 서버로 수량에 대한 데이터가 전송된다. (규격 설정)
 - 120초 내 결정을 눌러야 함 (time:120 과 같이 모든 플레이어에게 남은 시간 메시지를 보냄)

결정을 누른 이후:
 제한시간 내 모든 플레이어의 사고 팔기가 끝나면 아이템의 가격이 플레이어별로 표시되고, 서로의 손익 정보가 표시되는데 이 때 아이템의 가격 변동 폭은 랜덤으로 한다.

 - 아이템의 가격 정보가 모든 플레이어에게 메시지 형식으로 공지된다. (클라이언트에서는 해당 메시지를 띄움)
 - 서로의 손익 정보가 모든 플레이어에게 메시지 형식으로 공지된다. (클라이언트에서는 해당 메시지를 띄움)
 - 아이템의 가격 폭은 random으로 조절
 - 플레이어 DB는 서버에서 관리
'''


# 초고 서버
import socket, threading
import random

# 서버 주소, 포트
server_ip = '127.0.0.1'
server_port = 60000
address = (server_ip, server_port)

# 서버 연결 대기
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen()

# 플레이어 목록, 최대 인원수
client_list = []
client_score = []
max_per = 2 # 최대 인원

def connection():
    global client_list
    cnt = 0
    while cnt < max_per:
        client_socket, client_address = server_socket.accept()
        #client=[client_socket, client_address]
        #client_list.append(client)
        client_list.append(client_socket)
        print("Connected from {}".format(client_address))
        print("Now players are")
        for i in client_list:
            print(str(client_list.index(i)+1)+". ", end="")
            print(i)
        cnt = cnt + 1

def send_num(client_socket):
    num = random.randint(1,10)
    b_num = str(num).encode('utf-8')
    print(type(b_num))
    client_socket.send(b_num)

def receive(client_socket):
    try:
        data = client_socket.recv(1024)
        if data == (b"exit"):
            exit()
    except OSError:
        exit()
    print(data.decode('utf-8'))

connection()
print(1)

for i in client_list:
    send_num(i)
    
for i in client_list:
    B = threading.Thread(target=receive, args=(i,))
    B.start()
