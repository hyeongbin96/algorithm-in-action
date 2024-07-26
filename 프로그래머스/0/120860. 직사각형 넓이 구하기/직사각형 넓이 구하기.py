def solution(dots):
    # CASE A
    # x = [dots[0][0], dots[1][0], dots[2][0], dots[3][0]]
    # y = [dots[0][1], dots[1][1], dots[2][1], dots[3][1]]
    
    # CASE B
    # x, y = [], []
    # for i in dots:
    #     x.append(i[0])
    #     y.append(i[1])

    return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])