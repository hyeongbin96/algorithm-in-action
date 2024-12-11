import sys

N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

sorted_x = sorted(list(set(x)))
answer = {sorted_x[i]: i for i in range(len(sorted_x))}

for i in x:
    print(answer[i], end=" ")