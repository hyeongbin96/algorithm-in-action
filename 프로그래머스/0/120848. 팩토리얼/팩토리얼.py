def solution(n):
    sum = 1
    num = 1

    while sum <= n:
        num += 1
        sum *= num
        print(f"{num}! = {sum}")

    return num-1