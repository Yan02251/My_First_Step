'''

식별자와 변수명

식별자는 프로그래밍 언어에서 변수, 함수, 클래스, 모듈 등의 이름을 지칭하는 모든 명칭
변수명은 변수의 이름을 뜻한다.



import keyword
print(keyword.kwlist)

print("{}@{} {}".format(8,"기","백엔드"))

str = "{}".format(8)
print(str)



num = 8
str_a = "기"
str_b = "백엔드"

print(f"{num}{str_a} {str_b}")



print(type(777.777))


num_1 = 21
num_2 = 29
print ("{} + {} = {}".format(num_1,num_2,num_1+num_2))


num_1 = 21
num_2 = 29
print ("{} + {} = {}".format(num_1,num_2,num_1+num_2))



position = "백엔드"
get_in = "3명 타세요"

print(position + get_in * 3)



str ="초격차백엔드"

print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])


print(str[5])


print(len(str))


str ="초격차백엔드"

print(str[2:4])
print(str[0:7:2])



alpa = 'APP'

print (alpa.islower())
print (alpa.isupper())

answer = alpa.isupper()

print(answer)

'''

url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색하고 시은 키워드를 입력해줘 : ")

print(url+keyword)