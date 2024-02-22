# number = list(map(int,sys.stdin.readline().split())) 의미
# sys.stdin.readline() = 문자열로 입력 > 입력 값이 문자열로 들어옴
# sys.stdin.readline().split() = 입력 문자열을 공백으로 구분
# map(int, sys.stdin.readline().split()) = 입력 문자열을 정수형으로 변환
# list(map(int, sys.stdin.readline().split())) = 정수형으로 변환한 결과로 리스트를 생성
import sys

count = int(input())
number = list(map(int, sys.stdin.readline().split()))
v = int(input())

# sum = 0

# for key in number :
#     if key == v :
#         sum += 1

# print(sum)

print(number.count(v))