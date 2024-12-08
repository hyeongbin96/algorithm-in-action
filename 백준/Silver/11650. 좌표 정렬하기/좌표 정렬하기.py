import sys

N = int(input())
answer = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    answer.append([x, y])

for i in sorted(answer):
    print(*i)
