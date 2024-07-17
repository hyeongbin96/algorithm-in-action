def solution(balls, share):
    bunmo = number(balls - share) * number(share)
    bunja = number(balls)
    answer = bunja // bunmo
    return answer


def number(n):
    num = 1
    for i in range(n, 0, -1):
        num *= i
    return num
