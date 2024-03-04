# 최초 풀이
# N = int(input())
# number = list(map(int, input().split()))
# prime_number = []

# for i in number :
#     temp = []
#     for j in range(2, i+1) :
#         if i % j == 0 :
#             temp.append(j)
#         if sum(temp) == i :
#             prime_number.append(i)

# print(len(prime_number))

# 타인 답 참고 후 풀이
import sys

N = int(input())
number = list(map(int, sys.stdin.readline().split()))
prime_number = []

for i in number :
    for j in range(2, i+1) :    # 1은 무조건 나누어지기 때문에 2부터 시작, i까지 비교해야 하므로 i+1
        if i % j == 0 :         # number(i) 값을 2부터 number까지 나누어보면서 나머지가 0이면서 number(i)와 j가 동일할 때까지 반복
            if i == j :
                prime_number.append(j)
            break

print(len(prime_number))
