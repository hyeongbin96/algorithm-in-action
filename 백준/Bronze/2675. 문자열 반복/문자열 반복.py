import sys

T = int(input())

for i in range(T) :
    P = ''
    R, S = sys.stdin.readline().split()
    count = int(R)
    for j in S :
        P += j*count
    print(P)