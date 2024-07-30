from math import gcd

def solution(a, b):
    answer = b // gcd(a, b)
    while answer > 1:
        if answer % 2 == 0:
            answer = answer // 2
        elif answer % 5 == 0:
            answer = answer // 5
        else:
            return 2

    return 1