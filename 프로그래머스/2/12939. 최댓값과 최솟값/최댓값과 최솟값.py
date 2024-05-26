def solution(s):
    answer = [int(i) for i in list(s.split())]
    result = str(min(answer)) + ' ' + str(max(answer))
    return result