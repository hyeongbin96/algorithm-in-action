def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer


def gcd(n, m):
    r = 0
    while m != 0:
        r = n % m
        n = m
        m = r
    return n


def lcm(n, m):
    lcm = (n * m) // gcd(n, m)
    return lcm
