n, m = map(int, input().split())

a = []
b = []

for i in range(n) :
    key = list(map(int, input().split()))
    a.append(key)

for j in range(n) :
    key = list(map(int, input().split()))
    b.append(key)

for i in range(n) :
    for j in range(m) :
        print(a[i][j] + b[i][j], end=' ')
    print()