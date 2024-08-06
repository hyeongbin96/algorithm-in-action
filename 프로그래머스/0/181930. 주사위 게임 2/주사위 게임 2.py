def solution(a, b, c):
    answer = [a, b, c]
    sum = 0
    if a != b != c:
        sum = a + b + c
    if answer.count(a) == 2 or answer.count(b) == 2 and answer.count(c) == 2:
        sum = (a + b + c) * (a * a + b * b + c * c)
    if a == b == c:
        sum = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    return sum