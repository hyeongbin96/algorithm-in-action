def solution(a, b):
    a = sorted([a, b])
    return sum(i for i in range(a[0], a[1] + 1))