a, b = input().split()
reverse_a = ''
reverse_b = ''

for i in a :
    reverse_a = i + reverse_a

for j in b :
    reverse_b = j + reverse_b

if int(reverse_a) > int(reverse_b) :
    print(int(reverse_a))
else :
    print(int(reverse_b))