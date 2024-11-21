fish_brade = input("맛을 골라주세요. : ")
count = int(input("개수를 입력해주세요. : "))



stock = {
    "팥붕어빵" : 10,
    "슈크림" : 8,
    "초코붕어빵" : 5
    
}


stock["팥붕어빵"] += count
print(f'{fish_brade}맛을 {count}개 채워 현재 재고는 {stock[fish_brade]}개입니다.')
