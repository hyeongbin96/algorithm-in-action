def solution(strArr):
    answer = {}
    for word in strArr:
        if len(word) not in answer:
            answer[len(word)] = 1
        else:
            answer[len(word)] += 1
    return max(answer.values())