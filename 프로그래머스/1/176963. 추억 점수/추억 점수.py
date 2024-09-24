def solution(name, yearning, photos):
    answer = {}
    score = []

    for i in range(len(name)):
        answer[name[i]] = yearning[i]

    for photo in photos:
        score_sum = 0
        for i in photo:
            if i in answer:
                score_sum += answer[i]
        score.append(score_sum)

    return score