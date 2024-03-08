N = int(input())
x = []
y = []

for i in range(N) :
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

h = max(y) - min(y)
w = max(x) - min(x)

print(h*w)