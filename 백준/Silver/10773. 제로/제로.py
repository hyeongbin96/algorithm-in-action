import sys

K = int(sys.stdin.readline())

result = []

for _ in range(K) :
    num = int(sys.stdin.readline())
    if num == 0 :
        result.pop()
    else :
        result.append(num)

print(sum(result))