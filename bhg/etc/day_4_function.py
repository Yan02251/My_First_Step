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


def main():
    while Ture:
        mode = input("원하는 모드를 선택해주세요(주문, 관리자, 종료) : ")
        if mode == "종료":
             break
        if mode == "주문":
             order_bread()
        if mode == "관리자":
             manager_bread()

def order_bread():
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


def manager_bread ():
    while True:
            bread_type = input("추가할 붕어빵 종류를 입력하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵): ")
            if bread_type =="종료":
                break
            bread_count = int(input("추가할 붕어빵 개수를 입력하세요: "))
            stock[bread_type] += bread_count
            print(f"{bread_type}의 재고가 {bread_count}개 추가되어, 현재{stock[bread_type]}개 입니다. ")



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
       

print("시스템이 종료되었습니다.")

for bread_t in sales:
    sales_money = sales[bread_t] * price[bread_t]
    total_sales = sales_money


print(f"오늘의 총 판매 금액은{total_sales}입니다.")

'''


stock = {

    "팥붕어빵" : 10,

    "슈크림붕어빵" : 8,

    "초코붕어빵" : 5

}



sales = {

    "팥붕어빵" : 0,

    "슈크림붕어빵" : 0,

    "초코붕어빵" : 0

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

            bread_type = input("주문하실 붕어빵의 맛을 골라주세요(주문 가능한 맛 : 팥붕어빵, 슈크림붕어빵, 초코붕어빵) : ")

            if bread_type == "뒤로가기":

                break

            elif bread_type == "팥붕어빵" or bread_type == "슈크림붕어빵" or bread_type == "초코붕어빵": #값이 있어 참(True), 값이 없어 거짓(false)

                 bread_count = int(input("주문할 붕어빵 개수를 입력하세요 ")) #팥붕어빵 10개 입력받음



                 if stock[bread_type] >= bread_count: #  3(재고) >= 10(주문한 붕어빵) -> False  if 조건:

                    stock[bread_type] -= bread_count # 재고에서 주문받은 만큼의 붕어빵 개수를 빼는 코드

                    sales[bread_type] += bread_count # 주문받은 만큼 판 붕어빵의 개수를 추가하는 코드

                    print(f"{bread_type} {bread_count}개를 판매되었습니다.")

                 else:

                    result = bread_count - stock[bread_type]

                    print(f"죄송합니다. {bread_type}의 재고가 {result}개 부족합니다.")



                #남은 재고를 맛과 개수로 보여주는 코드를 작성해주세요 딕셔너리.items() -> for bread_type, bread_count in 딕셔너리.items() 키와 벨류

                 print("------------------------")

                 print("현재 재고는 아래와 같습니다.")

                 for bread_t, bread_c in stock.items():

                    print(f'{bread_t} : {bread_c}')

                 print("------------------------")

            else:

                print("3가지 붕어빵 중에 선택해주세요")



    if mode == "관리자":

        pass



print("시스템이 종료되었습니다.")

