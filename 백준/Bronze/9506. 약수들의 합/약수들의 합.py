while True :
    number = int(input())
    divisor = [i for i in range(1, number) if number % i == 0]
    if number == -1 :
        break
    elif sum(divisor) == number :
        print(number, '=', end=' ')
        print(*divisor, sep=' + ')
    else :
        print(f'{number} is NOT perfect.')