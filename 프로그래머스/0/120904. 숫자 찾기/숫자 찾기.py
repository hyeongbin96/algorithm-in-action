def solution(num, k):
    answer = 0
    for idx, value in enumerate(str(num)):
        if value == str(k):
            answer = int(idx) + 1
            break
        else:
            answer = -1
    return answer
