import os, random

item_list = {'커피': 5, '밀가루': 5, '희토류': 5, '석유': 5, '소고기': 5, '시멘트': 5, '알루미늄': 5, '강철': 5}
turns = 5

def trading(item_list):
    pass
'''
사용자에게 사자/팔자, 아이템, 수량을 입력받아
현재 사용자의 리스트를 반환해 줌 (사고 판 내역도 정산해야 하므로 이 또한 고려할 것)
'''

def get_price_change(item_list):
    '''
    각 턴에서 사용될 파일 2개 만들기
    1. 물건 시세 변동여부와 공급/수요 여부 텍스트 파일
    2. 가격 변동 여부(-1/1) 파일 만들기
    '''
    # global turns

    flist = os.listdir('price_data')

    for file in flist:
        fr = open('price_data\\' + file, 'r')
        lines = fr.readlines()
        random.shuffle(lines)
        fr.close()

        fw = open('price_data\\' + file, 'w')
        fw.write(lines)
        fw.close()

    for cnt in range(turns):
        new_text = 'price_text_' + str(cnt) + '.txt'
        new_updown = 'price_updown_' + str(cnt) + '.txt'

        fw_text = open('price_text\\' + new_text, 'w')
        fw_updown = open('price_updown\\' + new_updown, 'w')

        for file in flist:
            fr = open('price_data\\' + file, 'r')
            lines = fr.readlines()
            price = lines[cnt]
            fw_text.write(price)

            tag = price.split('(')[1]
            change = tag.split()[1]
            if tag.startswith('수요 증가') or tag.startswith('공급 감소'):
                fw_updown.write('가격 증가')
            else:
                fw_updown.write('가격 감소')
            fr.close()

        fw_text.close()
        fw_updown.close()

def print_price_text(turns):
    '''
    물건 시세 변동 여부와 공급/수요 여부 텍스트 파일 출력하기
    '''

    file = 'price_text_' + str(turns) + '.txt'
    fr = open('price_text\\' + file, 'r')
    while True:
        line = fr.readline()
        if not line:
            break
        print(line)
    fr.close()

def read_price_text(val):
    # val: 아이템명 (beef, coffee, rare earth, etc...)
    # ref: Millstone Project (oop-project-ex)
    list = []
    f = open('./news/'+str(val), 'r', encoding="UTF-8")
    while True:
        newline = f.readline()
        if not newline:
            break
        list.append([newline.split('|')[0], int(newline.split('|')[1]), int(newline.split('|')[2]), int(newline.split('|')[3])])
        # coffee-1 | 브라질이 최악의 가뭄을 경험하고 있다.| 공급 | image/coffee/drought.png

    return list

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
