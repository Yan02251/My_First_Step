
'''
fish_bread = input("맛을 골라주세요. : ")
count = int(input("개수를 입력해주세요. : "))



stock = {
    "팥붕어빵" : 10,
    "슈크림" : 8,
    "초코붕어빵" : 5
    
}


stock["팥붕어빵"] += count
print(f'{fish_bread}맛을 {count}개 채워 현재 재고는 {stock[fish_bread]}개입니다.')
'''



stock = {
    "팥붕어빵" : 10,
    "슈크림붕어빵" : 10,
    "초코붕어빵" : 10
}

sales = {
    "팥붕어빵" : 3,
    "슈크림붕어빵" : 2,
    "초코붕어빵" : 2
}

price = {
    "팥붕어빵" : 1000,
    "슈크림붕어빵" : 1200,
    "초코붕어빵" : 1500
}

while True:
    mode = input("원하는 모드를 선택해주세요(주문, 관리자, 종료) : ")
    if mode == "종료":
        break
    if mode == "주문":
        while True:
            bread_type = input("주문하실 붕어빵의 맛을 골라주세요.(주문 가능 맛 : 팥붕어빵, 슈크림붕어빵, 초코붕어빵)")
            if bread_type == "뒤로가기":
                break
            bread_count = int(input("주문할 붕어빵 개수를 입력하세요."))


            if stock[bread_type] >= bread_count:
                stock[bread_type] -= bread_count
                sales[bread_type] += bread_count
                print(f"{bread_type} {bread_count}개가 판매되었습니다.")
            else:
                result = bread_count - stock[bread_type]
                print(f"죄송합니다. {bread_type}의 재고가 {result}개 부족합니다.")

            print("현재 재고는 아래와 같습니다.")
            for bread_t, bread_c in stock.items():
                print(f'{bread_t} : {bread_c}')
            else:
                print("3가지 붕어빵 중에 선택해주세요")

    if mode == "관리자":
        while True:
            bread_type = input("추가할 붕어빵 종류를 입력하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵): ")
            if bread_type =="종료":
                break
            bread_count = int(input("추가할 붕어빵 개수를 입력하세요: "))
            stock[bread_type] += bread_count
            print(f"{bread_type}의 재고가 {bread_count}개 추가되어, 현재{stock[bread_type]}개 입니다. ")

print("시스템이 종료되었습니다.")

for bread_t in sales:
    sales_money = sales[bread_t] * price[bread_t]
    total_sales = sales_money


print(f"오늘의 총 판매 금액은{total_sales}입니다.")


