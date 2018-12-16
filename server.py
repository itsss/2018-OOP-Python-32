'''
게임 시작 전:
 - 사용자가 방에 입장하는 경우 모든 플레이어에게 (접속한 플레이어 모두) 접속자 명단을 보냄
 - 최대인원이 찬 경우 더 이상 입장할 수 없도록(?) - 최대 인원수 제한을 둠으로서 해결
 - 최대인원이 차면 20초 내 게임을 시작함 (time:20 등과 같이 모든 플레이어에게 남은 시간 메시지를 보냄) - 5초 후 게임 시작 표현(완료)
 * 채팅 기능 추가

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
# 방 최대 인원 추가
# 채팅 기능 추가 - 현재 작업중
# 턴 함수 구조 중
# - 8개 종목에서 각각 한 사례 뽑아서 전송하는 함수 (완료)
# - 해당 사례가 가격 상승/하락임을 읽고 가격 정하는 함수 (미구현)
# - 시간 제한 함수 (미구현)
# - 클라이언트에게서 데이터 변화량을 받는 함수 (완료)
# - 판매 구매 수치를 점수(돈)으로 계산하는 함수 (미구현)

import socket
import threading
import random
import time

# 서버 주소, 포트
server_ip = '127.0.0.1'
server_port = 60043
address = (server_ip, server_port)

# 서버 연결 대기
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen()

# 플레이어 목록, 최대 인원수
client_list = []
client_item=[]
client_score = [0,0,0,0,0,0,0,0]
max_per = 1
val = []
#초기 가격
#item = ['소고기', '커피', '희토류', '밀가루', '시멘트', '알루미늄', '강철', '석유']
price=[5,5,5,5,5,5,5,5]
cnt = 0

#종목의 데이터 정보를 저장하고 있는 리스트
type_list=[[[11,1],[12,-1],[13,1],[14,-1],[15,-1]],
            [[21,1],[22,-1],[23,-1],[24,1],[25,-1]],
           [[31,1],[32,-1],[33,1],[34,-1],[35,1]],
           [[41,-1],[42,1],[43,1],[44,-1],[45,-1]],
           [[51,1],[52,1],[53,-1],[54,1],[55,-1]],
           [[61,-1],[62,1],[63,-1],[64,-1],[65,-1]],
           [[71,-1],[72,1],[73,-1],[74,1],[75,-1]],
           [[81,-1],[82,1],[83,1],[84,-1],[85,-1]]]
# 플레이어로부터 데이터를 받아 나머지에게 전송
#채팅 기능이 방이 들어올때까지만 구현되었습니다... 데이터 섞일 일은 없을 거에요
def server_chat(client_socket):
    global client_list
    global cnt

    # 접속 종료 여부 확인 변수
    impos = 0
    while cnt < max_per:
        try:
            data = client_socket.recv(1024)
            # 만약 "exit"을 받으면 접속 종료 표기
            if data.decode('utf-8') == "exit":
                print("{} disconnect".format(client_socket))
                impos = 1
                break
        # 오류가 날 경우 접속 종료 표기
        except KeyboardInterrupt:
            impos = 1
            break
        except ConnectionError:
            impos = 1
            break
        # 받은 데이터 / 채팅을 나를 제외한 플레이어에게 전송
        for i in client_list:
            if not i == client_socket:
                data=data.decode('urf-8')
                i.send(data.encode('utf-8'))
    # 만약 접속 종료 표기가 있으면 소켓을 닫는다.
    if impos:
        cnt = cnt - 1
        client_socket.close()
        client_list.remove(client_socket)
        print("{} has disconnected".format(client_socket))

# 플레이어의 연결을 수행
def connection():
    global client_list
    global cnt
    global val

    while cnt < max_per:
        client_socket, client_address = server_socket.accept()
        # client=[client_socket, client_address]
        # client_list.append(client)
        client_list.append(client_socket)
        val.append([0,0,0,0,0,0,0,0])
        client_socket.send(b"Welcome to economic server!\n")
        client_socket.send(b"If you want to exit, try \"exit\".")

        cnt = cnt + 1

        #클라이언트 정보를 서버에서 출력
        print("Connected from {}".format(client_address))
        print("Now %d players join. List:" % cnt)
        for i in client_list:
            print(str(client_list.index(i) + 1) + ". ", end="")
            print(i)

        Se = threading.Thread(target=server_chat, args=(client_socket,))
        Se.start()
    print("All player joined! Server is starting game...")


# 게임 시작을 플레이어에게 알림
# 5초 후 게임을 시작함
def game_start(client):
    client.send(b"All player joined! Server is starting game...")
    for t in range(5, 0, -1):
        client.send(str(t).encode('utf-8'))
        time.sleep(1)
    client.send(b"start")

#랜덤값을 뽑아 클라이언트에게 보내는 함수
#리스트에 저장된 종목의 데이터를 뽑아 클라이언트에게 전송한다.
#수정 필요 // 데이터를 새로 뽑아야 합니다아
def send_type_num():
    # global type_list
    type_list = [[[11, 1], [12, -1], [13, 1], [14, -1], [15, -1]],
                 [[21, 1], [22, -1], [23, -1], [24, 1], [25, -1]],
                 [[31, 1], [32, -1], [33, 1], [34, -1], [35, 1]],
                 [[41, -1], [42, 1], [43, 1], [44, -1], [45, -1]],
                 [[51, 1], [52, 1], [53, -1], [54, 1], [55, -1]],
                 [[61, -1], [62, 1], [63, -1], [64, -1], [65, -1]],
                 [[71, -1], [72, 1], [73, -1], [74, 1], [75, -1]],
                 [[81, -1], [82, 1], [83, 1], [84, -1], [85, -1]]]
    now_list=[]
    send_str="DATA|"

    for i in type_list:
        #리스트에 있는 값을 뽑고
        #리스트에서 삭제, 반환할 리스트에 저장
        type=random.choice(i)
        now_list.append(type)
        send_str += str(type[0])+"/"
        i.remove(type)
    return now_list, send_str



#클라이언트에게서 사고판 수량을 받는 함수
def receive_selling(client, num):
    global val
    try:
        #받는 데이터 형태는 b"a:b/c:d/ ... /p:q"
        data=client.recv(1024)
    except OSError:
        exit()
    data = data.decode('utf-8')
    data2 = data[5:]
    #받은 문자열을 / 단위로 스플릿 후
    data3 = data2.split("/")
    #구매/판매 수량을 변화 리스트에 저장
    for i in range(0, 8):
        temp = data3[i].split(":")
        val[num][i] += int(temp[0]) - int(temp[1])

#기존 수량과 변화 수량을 받아 판매/구매 후의 수량을 반환하는 함수
def update_value(bef, cha):
    aft=[]
    for i in range(0,8):
        aft.append(bef[i]-cha[i])
    return aft

#가격을 변화시키는 함수
#p id 현재가격, q 부호
def random_price(p, q):
    min_val=1
    max_val=5
    if q < 0:
        if p==1:
            return 0
        max_val = min(p-1, max_val)
    change=random.randint(min_val,max_val)
    return change*q

#턴 함수
def turn():
    global client_list
    global client_score
    global price
    global symbol
    global val

    #가격 추이 번호 선정
    now_type_list, send_data = send_type_num()
    for i in client_list:
        i.send(send_data.encode('utf-8'))

    price_change=[]
    #변경되는 가격 리스트
    for i in range(0,8):
        price_change.append(random_price(price[i], now_type_list[i][1]))
    #가격 변경
    for i in range(0,8):
        price[i]=price[i]+price_change[i]

    #클라이언트에게서 받는 사고 판 리스트
    for i in range(0, max_per):
        #사기/팔기 데이터를 읽어오기
        get_data=threading.Thread(target=receive_selling, args=(client_list[i],i,))
        get_data.start()
        get_data.join()

    for i in client_list:
        #시세표
        now_price="PRICE|"
        for j in range(0,8):
            now_price += str(price[j])+"/"
        i.send(now_price.encode('utf-8'))
        #수익

    for i in range(0, max_per):
        p = 0
        for j in range(0, 8):
            p = p + val[i][j] * price_change[j]
        sn_data = "PL|"+str(p)
        client_list[i].send(sn_data.encode('utf-8'))
        #최종 수익 변경
        time.sleep(0.5)

    for j in range(0, max_per):
        client_score[j] += price_change[j]

    max_list=sorted(client_score)
    max_list.reverse()

    for i in client_list:
        #점수 클라이언트에게 보내기
        for j in range(0,max_per):
            i.send(str(max_list[j]).encode('utf-8'))
            time.sleep(0.5)
connection()
# rand_num=random.randint(1,10)
# send_num(rand_num, i)

for i in client_list:
    A = threading.Thread(target=game_start, args=(i,))
    A.start()

turn_cnt=0
while turn_cnt<5:
    turn()
    turn_cnt=turn_cnt+1

score = 'END|'
for i in range(0, max_per):
    score += str(client_score[i]) + '/'

for i in client_list:
    i.send(score.encode('utf-8'))

