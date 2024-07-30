def solution(score):
    answer = []
    for i in range(len(score)):
        score[i] = sum(score[i]) / 2

    answer = sorted(score, reverse=True)

    rank = []

    for i in range(len(answer)):
        rank.append(answer.index(score[i]) + 1)

    return rank