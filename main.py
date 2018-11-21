def get_input(current_list):
    pass
'''
사용자에게 사자/팔자, 아이템, 수량을 입력받아
현재 사용자의 리스트를 반환해 줌 (사고 판 내역도 정산해야 하므로 이 또한 고려할 것)
'''
    # buy = 0
    # sale = 0
    # print('커피, 밀가루, 희토류, 석유, 소고기, 시멘트, 알루미늄, 강철')
    # met = input()
    #
    # if str(met) == "exit":
    #     print("Thank you for using this program")
    #     print("End of the Game")
    #     exit()
    #
    # else:
    #     meth, inp, price = met.split(" ")
    #     if str(meth) == "buy":
    #
    #     if str(meth) == "sale":
    #
    #

def print_status():
    pass
'''
물건의 공급/수요 출력
'''

def print_price():
    pass
'''
물건 시세 변동 여부 출력
'''

def get_ind_score():
    pass

'''
개인별 점수 구하기
'''

def print_ind_score():
    pass
'''
개인별 점수 출력 (매 턴마다)
'''

def print_all_score():
    pass
'''
전체에게 사용자 점수 출력 (매 턴마다)
'''

def final_score():
    pass
'''
(최종 점수 출력)
플레이어 최종 이득(점수) 출력
최종수익 (판매액 - 구매액)
'''

print('='*50)
print('economic game')
print('='*50)

while True:
    current_list = [5, 5, 5, 5, 5, 5, 5, 5]
    curr, deal = get_input(current_list)

'''
Main 함수 출력
'''