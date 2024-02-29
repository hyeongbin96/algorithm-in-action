N = int(input())

count = 1
sum = 1

if N == 1:
    count = 1
else :
    while N > sum :
        sum += (6*count)
        count += 1

print(count)