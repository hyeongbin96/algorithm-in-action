def solution(order):
    answer = [i for i in str(order) if int(i) in (3,6,9)]
    return len(answer)