def get_input(item_list):
'''
사용자의 구매/판매를 시행하는 함수
사용자로부터 구매/판매와 수량을 입력받아 물건 내역을 업데이트
'''
    #누적 판매량과 누적 구매량
    sale=0
    buy=0
    for item in item_list:
        #판매/구매/취소를 입력
        while True:
            try:
                trade, amount = input.split()
            except :

            if str(trade) == 'none':
                break
            now=item_list[item]
            if str(trade) == "buy":
                #누적 구입량이 5를 넘어서는 구매인 경우
                if(amount+buy>5):
                    print("You have exceeded the purchase limit. Please enter again.")
                    break
                #구입량만큼 해당 아이템 수 증가, 누적 구입량 증가
                item_list[item].update({item_list[item]:now+amount})
            sale=sale+amount
            if str(trade) == "sale":
                #현재 수량보다 많은 수랴을 파는 경우
                if(amount>now):
                    print("Quantity is insufficient. Please enter again.")
                    break
                #누적 판매량이 10을 넘어서는 판매인 경우
                if(amount+sale>10):
                    print("You have exceeded the sale limit. Please enter again.")
                    break
                #판매량만큼 해당 아이템 수 감소, 누적 판매량 증가
                item_list[item].update({item_list[item]:now-amount})
                buy=buy+amount
        break
