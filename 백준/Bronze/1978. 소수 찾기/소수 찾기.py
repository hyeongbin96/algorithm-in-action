import sys

N = int(input())
number = list(map(int, sys.stdin.readline().split()))
prime_number = []

for i in number :
    for j in range(2, i+1) :
        if i % j == 0 :
            if i == j :
                prime_number.append(j)
            break

print(len(prime_number))