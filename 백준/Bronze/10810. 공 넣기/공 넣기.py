n, m = map(int, input().split())
basket = [0] * n

for i in range(1, m+1) :
    i, j, k = map(int, input().split())
    for count in range(i-1, j) :
        basket[count] = k

print(*basket)