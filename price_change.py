#sd는 가격 변동 리스트입니다 1이면 상승, -1이면 하락 ex) sd=[1, -1, 1, -1, -1, 1, -1, 1]

import random

def price_change(sd, item_price):
    """
    수요와 공급의 변동으로 인한 가격 변동을 1/-1으로 입력받아
    주어진 범위 내에서 랜덤한 수만큼 가격 상승 / 하락
    :param sd: 가격 상승/하락 여부를 저장하는 리스트
    :param item_price:물건 기존(전 턴까지) 가격
    """
    #카운팅 변수
    cnt=0
    for item in item_price:
        #최초 상승/하락폭의 최대값과 최솟값 /10000으로 나눈 값
        max_value = 10
        min_value = 1
        #만약 가격이 하락한 경우
        #최대 하락폭이 현재 가격보다 크다면 10000 낮도록 교환, 즉 가격은 10000원 이하로 내려갈 수 없음
        if sd[cnt]==-1:
            max_value=min(max_value, item_price[item]/10000-1)
        #주어진 범위 내에서 랜덤하게 변동
        change=random.randint(min_value, max_value)
        item_price[item]=item_price[item]+change*sd[cnt]*10000
        cnt=cnt+1
