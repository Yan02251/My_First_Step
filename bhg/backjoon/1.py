A = int(input("첫번째 정수를 입력하세요: "))
B = int(input("더할 두번째 정수를 입력하세요: "))
print(f"두 정수의 합은 {A + B}입니다.")

except ValueError:
    print("올바른 정수를 입력해주세요.")

""""""


# 두 정수를 입력받아 A, B에 저장
A, B = map(int, input().split())

# 입력값 조건 검증
if 0 < A < 10 and 0 < B < 10:
    print(A + B)
else:
    print("입력값은 0보다 크고 10보다 작은 정수여야 합니다.")