N = int(input())

for i in range(1, N+1) :
    num = list(map(int, str(i)))
    result = sum(num) + i
    if N == result :
        print(i)
        break
    else :
        if N == i :
            print(0)