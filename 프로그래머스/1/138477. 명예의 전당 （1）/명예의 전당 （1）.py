def solution(k, score):
    answer = []
    result = []
    
    for i in range(len(score)):
        if i < k:
            answer.append(score[i])
        else:
            answer.append(score[i])
            answer.remove(min(answer))
        answer.sort()
        result.append(answer[0])

    return result
