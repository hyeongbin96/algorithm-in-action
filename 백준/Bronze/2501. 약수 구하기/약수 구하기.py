N, K = map(int, input().split())

# number = [i for i in range(1, N+1) if N % i == 0] for 문을 사용하지 않고 이처럼 해도 됨
number = []

for i in range(1, N+1) :
    if N % i == 0:
        number.append(i)
    
if len(number) < K :
    print(0)
else :
    print(number[K-1])
