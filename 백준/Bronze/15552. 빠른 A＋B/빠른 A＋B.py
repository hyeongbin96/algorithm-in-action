# input대신 sys.stdin.readline을 사용할 수 있다. 
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 rstrip()을 추가로 해 주는 것이 좋다.
# input = sys.stdin.readline()

import sys
count = int(input())

for i in range(count) :
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)