def solution(balls, share):
    answer = number(balls) // (number(balls - share) * number(share))
    return answer


def number(n):
    num = 1
    for i in range(n, 0, -1):
        num *= i
    return num