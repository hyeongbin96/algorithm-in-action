# print(*리스트) > 리스트의 요소들을 한번에 출력

import sys

n, x = map(int, input().split())
number = list(map(int, sys.stdin.readline().split()))
result = []

for key in number :
    if key < x :
        result.append(key)

print(*result)