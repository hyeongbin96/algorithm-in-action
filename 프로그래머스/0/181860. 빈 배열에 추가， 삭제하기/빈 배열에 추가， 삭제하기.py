def solution(arr, flag):
    answer = []
    for idx, bool in enumerate(flag):
        if bool == True:
            answer += [arr[idx]] * (arr[idx] * 2)
        else:
            for i in range(arr[idx]):
                answer.pop()

    return answer