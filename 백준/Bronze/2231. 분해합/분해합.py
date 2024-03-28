N = int(input())

for i in range(1, N+1) :
    number = list(map(int, str(i)))
    if N == sum(number) + i :
        print(i)
        break
    else :
        if i == N :
            print(0)