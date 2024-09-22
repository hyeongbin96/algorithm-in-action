def solution(s):
    answer = []
    ori = ""
    for idx, word in enumerate(s):
        if word not in ori:
            answer.append(-1)
        else:
            answer.append(idx - ori.index(word))
            ori = ori.replace(word, "#", idx)
        ori += word

    return answer