def solution(dots):
    answer = []
    dots.sort()
    a, b, c, d = dots

    for i in range(len(dots)):
        g1 = (a[0] - b[0]) / (a[1] - b[1])
        g2 = (c[0] - d[0]) / (c[1] - d[1])
        if g1 == g2:
            answer.append(1)

    return 1 if 1 in answer else 0