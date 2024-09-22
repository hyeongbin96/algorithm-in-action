def solution(s):
    answer = []
    dic = dict()
    for idx, word in enumerate(s):
        if word not in dic:
            answer.append(-1)
        else:
            answer.append(idx - dic[word])
        dic[word] = idx

    return answer