import sys
N, M = map(int, input().split())
card = list(map(int, input().split()))
num = []

for i in range(N) :
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            result = card[i] + card[j] + card[k]
            if result > M :
                continue
            else :
                num.append(result)
    
print(max(num))