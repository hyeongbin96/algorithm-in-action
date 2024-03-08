a = []

for i in range(3) :
    gak = int(input())
    a.append(gak)

if 0 in a or sum(a) != 180 :
    print('Error')
elif a[0] == a[1] == a[2] :
    print('Equilateral')
elif a[0] == a[1] and a[0] != a[2] or a[0] == a[2] and a[0] != a[1] or a[1] == a[2] and a[0] != a[1] :
    print('Isosceles')
else : 
    print('Scalene')