def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] is True:
            answer += a
        a += d
    return answer
