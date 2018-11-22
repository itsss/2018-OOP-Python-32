#일단 구매 판매하는 함수는 만들었습니다.
#근데 이번 턴의 수익을 확인하기 위해 상품 판매수/구입수를 반환 추가 필요.

def trading(item_list):
    """
    사용자의 구입/판매를 시행하는 함수
    사용자로부터 구입/판매와 수량을 입력받아 물건 수량을 업데이트
    """
    # 누적 판매량과 구입량
    sale = 0
    buy = 0
    # 최대 판매 제한량과 구매 제한량
    limit_sale = 10
    limit_buy = 5

    for item in item_list:
        # 판매/구입/취소를 입력
        while True:
            now = item_list[item]
            # 매 상품마다 상품의 종류와 보유 수량을 표시
            # 남은 구입 제한, 판매 제한을 표시
            print("Trading item: [%s] remain: [%s] left" % (item, now))
            print("purchase limit: %d" % (limit_buy - buy))
            print("Sale limit: %d" % (limit_sale - sale))
            # 일단 넣어뒀습니다만 나중에 오류나면 추가하는 걸로@@@@@@
            try:
                trade, amount = input().split()
            except ValueError:
                break
            if trade == 'none':
                break
            # 문자로 입력받은 수량을 정수로 전환
            amount = int(amount)
            if trade == "buy":
                # 누적 구입량이 구매 제한량을 넘어서는 경우
                if (amount + buy > limit_buy):
                    print("You have exceeded the purchase limit. Please enter again.\n")
                    continue
                # 구매량만큼 해당 아이템 수 증가, 누적 구입량 증가
                item_list[item] = now + amount
                buy = buy + amount
            elif trade == "sale":
                # 보유 수량보다 판매 수량이 큰 경우
                if (amount > now):
                    print("Quantity is insufficient. Please enter again.\n")
                    continue
                # 누적 판매량이 판매 제한량을 넘어서는 경우
                if (amount + sale > limit_sale):
                    print("You have exceeded the sale limit. Please enter again.\n")
                    continue
                # 판매량만큼 해당 아이템 수 감소, 누적 판매량 증가
                item_list[item] = now - amount
                sale = sale + amount
            else:
                print("Please enter again.")
                continue
            break
