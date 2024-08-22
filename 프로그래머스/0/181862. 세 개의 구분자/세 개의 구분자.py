def solution(myStr):
    answer = []
    words = ""

    for i in range(len(myStr)):
        if myStr[i] != "a" and myStr[i] != "b" and myStr[i] != "c":
            words += myStr[i]
        else:
            answer.append(words)
            words = ""
    answer.append(words)

    if len([i for i in answer if i != ""]) == 0:
        return ["EMPTY"]
    else:
        return [i for i in answer if i != ""]