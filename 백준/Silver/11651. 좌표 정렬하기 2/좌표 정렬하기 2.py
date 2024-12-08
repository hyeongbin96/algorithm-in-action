import sys

N = int(input())
answer = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    answer.append([x, y])

answer.sort(key=lambda x: (x[1], x[0]))

for i in answer:
    print(*i)
