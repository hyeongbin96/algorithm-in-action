def solution(dots):
    x = [dots[0][0], dots[1][0], dots[2][0], dots[3][0]]
    y = [dots[0][1], dots[1][1], dots[2][1], dots[3][1]]
    return (max(x) - min(x)) * (max(y) - min(y))
