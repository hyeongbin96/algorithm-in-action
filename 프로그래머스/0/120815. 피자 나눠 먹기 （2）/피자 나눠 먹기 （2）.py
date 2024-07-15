import math

def solution(n):
    gcd = math.gcd(6, n)

    if n % 6 == 0:
        answer = n // 6
    else:
        answer = ((n * 6) // gcd) // 6
        
    return answer