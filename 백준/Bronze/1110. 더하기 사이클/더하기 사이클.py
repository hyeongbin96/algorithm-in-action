N = int(input())

num = N
count = 0

while True :
    a = num % 10
    b = ((num // 10) + (num % 10)) % 10
    num = int(str(a) + str(b))
    if num == N :
        count += 1
        print(count)
        break
    else :
        count += 1