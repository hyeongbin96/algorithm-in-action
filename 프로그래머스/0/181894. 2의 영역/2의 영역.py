def solution(arr):
    answer = []
    for idx, v in enumerate(arr):
        if v == 2:
            answer.append(idx)
    if len(answer) == 0:
        return [-1]
    return arr[answer[0] : answer[-1] + 1]