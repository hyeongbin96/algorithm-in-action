def solution(answers):
    answer = []
    result = {"1": 0, "2": 0, "3": 0}
    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    for i in range(len(answers)):
        if answers[i] == a[i]:
            result["1"] += 1
        if answers[i] == b[i]:
            result["2"] += 1
        if answers[i] == c[i]:
            result["3"] += 1

    for k, v in result.items():
        if v == max(result.values()):
            answer.append(int(k))

    return answer
