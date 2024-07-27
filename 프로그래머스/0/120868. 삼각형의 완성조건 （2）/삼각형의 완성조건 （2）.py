def solution(sides):
    a = max(sides) - (max(sides) - min(sides))
    b = (sum(sides) - 1) - max(sides)
    return a + b