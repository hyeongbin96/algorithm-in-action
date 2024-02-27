N, B = input().split()
B = int(B)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0
index = len(N)

for i in range(len(N)) :
    sum = (number.index(N[i])) * (B**(index-1))
    index -= 1
    result += sum

print(result)