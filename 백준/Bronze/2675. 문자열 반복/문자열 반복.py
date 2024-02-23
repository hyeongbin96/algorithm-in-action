import sys

T = int(input())

for i in range(T) :
    P = ''
    R, S = sys.stdin.readline().split()
    count = int(R)
    for j in S :
        P += j*count
    print(P)

# 다른 풀이자의 답
# > 더 효율적이고 간결한거 같음
    
# T = int(input())

# for i in range(T) :
#     R, S = input().split()
#     for j in range(len(S)) :
#         print(S[j]*int(R), end='')
#     print()
