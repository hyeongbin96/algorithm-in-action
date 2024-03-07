a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

x = [a, c, e]
y = [b, d, f]

if x[0] == x[1] :
    first = x[2]
elif x[1] == x[2] :
    first = x[0]
else :
    first = x[1]

if y[0] == y[1] :
    second = y[2]
elif y[1] == y[2] :
    second = y[0]
else :
    second = y[1]

print(first, second)