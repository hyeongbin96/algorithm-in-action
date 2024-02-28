alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 33, 2
N, B = map(int, input().split())
result = []

while True :
    if N >= B :
        remainder = (N % B)
        result.append(remainder)
        N = (N // B)
    else :
        result.append(N)
        break

result.reverse()

for i in result :
    print(alpha[i], end='')