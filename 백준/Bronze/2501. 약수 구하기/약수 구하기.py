N, K = map(int, input().split())

number = []

for i in range(1, N+1) :
    if N % i == 0:
        number.append(i)
    
if len(number) < K :
    print(0)
else :
    print(number[K-1])