'''

[문제 1: 잔액 확인]

현재 잔액은 1000원입니다. 현재 잔액을 출력하세요. (변수명 예시 : 잔액 - balance)

'''



receipts = []
balance = 1000

while True:

    num = int(input("사용하실 기능을 선택해주세요 (1: 입금, 2: 출금, 3: 영수증 보기)"))
    if num == 1:
    #입금 기능
        deposit_amount = int(input("입금할 금액을 입력해주세요."))
        balance += deposit_amount
        receipts.append(("입금",deposit_amount,balance))


        num = int(input("사용하실 기능을 선택해주세요 (1: 입금, 2: 출금, 3: 영수증 보기"))
    elif num == 2:
        withdraw_amount = int(input("출금할 금액을 입력해주세요."))
        withdraw_amount = min(balance,withdraw_amount)
        balance -= withdraw_amount
        receipts.append(("출금",withdraw_amount,balance))

        print(f'출금하신 금액은 {withdraw_amount}입니다. 현재 잔액은 {balance }입니다.')

        print(receipts)