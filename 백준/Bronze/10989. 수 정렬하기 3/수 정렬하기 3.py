import sys

N = int(sys.stdin.readline())

numbers = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    numbers[num] += 1

for i in range(1, 10001):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)
