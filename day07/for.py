# ram : 변수[데이터 타입], random
# cpu : 연산자, 명령문(), 조건문, 반복문[for]

for x in range(10):
    print(x)
print("끝") # 1~ 9까지 출력후 '끝' 출력

# n = int(input("몇번까지 출력할까요?:")) + 1
# for x in range(n):
#     print(x)

# 배수 출력하기
# n = int(input("수 입력:"))
# for x in range(1001):
#     if x % n ==0:
#         print(x)


sum = 0
n = int(input("수 입력:"))
m = int(input("수 입력:"))
for x in range(n + 1):
    if x % m == 0:
        sum += x
print(sum)


# 0~10000 사이의 숫자 6개 가진 리스트를 출력 ---> 내일



