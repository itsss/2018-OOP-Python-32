import socket
import requests
import time

class server:
    #서버 주소
    ip='127.0.0.1'
    port=50000
    self.address=(ip, port)

    #서버 연결 준비
    server_socket=socket.socket=(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(addrss)
    server_socket.listen()

    #플레이어 목록, 최대 인원수
    client_list=[]
    client_score=[]
    max_per=8
    cnt=0

    def score_recv(client_socket):
        global client_score
        try:
            data=client_socket.recv()
        except ConnectionError:
            print("{} had disconnected".format(client_socket))
            exit()
        data.decode('UTF-8')
        for i in client_score:
            if i[0]==client_socket:
                i[1]=i[1]+int(data)
                break

    def conection():
        global client_list
        #최대 인원수가 되기 전까지 플레이어 입력
        while cnt<max_per:
            client_socket, client_address=server_socekt.accept()
            client_socket.send(b"You connected in economic server!")

            client_list.append(client_socket)
            #전체 플레이어에게 게임 참여 출력
            for c in client_list:
                c.send(b"{} joins to game".format(client_socket))
            cnt=cnt+1


#접속자 입력받고
#전체 플레이어에게 입장 여부 출력
#최대 인원 제한
