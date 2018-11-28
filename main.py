import os, random

item_list = {'커피': 5, '밀가루': 5, '희토류': 5, '석유': 5, '소고기': 5, '시멘트': 5, '알루미늄': 5, '강철': 5]
turns = 5
             
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

def get_price_change(item_list): 
'''
각 턴에서 사용될 물건 시세 변동여부와 공급/수요 여부 텍스트 파일을 만들기
'''
    gloabal turns 
             
    flist = os.listdir('price_data')

    for file in flist:
        fr = open('price_data\\' + file, 'r')
        lines = fr.readlines()
        random.shuffle(lines)
        fr.close()

    for cnt in range(turns):
        newname = 'price_change_' + str(cnt) + '.txt'
        fw = open('price_change\\' + newname, 'w')
        
        for file in flist:
            name = os.path.split(file)[0]
            fr = open('price_data\\' + file, 'r')
            lines = fr.readlines()
            price = name + ':' + lines[cnt]
            fw.write(price)
            fr.close()
             
        fw.close()
             
def print_price_text(turns):
    '''
    물건 시세 변동 여부와 공급/수요 여부 텍스트 파일 출력하기
    '''

    file = 'price_change_' + str(turns) + '.txt'
    fr = open('price_change\\' + file, 'r')
    while True:
        line = fr.readline()
        if not line: 
            break
        print(line)
    fr.close()

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
(최종 순위 출력)
플레이어 최종 이득(점수) 출력
최종수익 (판매액 - 구매액)
'''

print('='*50)
print('economic game')
print('='*50)

get_price_change(item_list)

for i in range(turns):
    print_price_text(i)
    trading(item_list)
    print_ind_score()
    print_all_score()
    
final_score()

'''
Main 함수 출력
'''
