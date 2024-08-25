def solution(rank, attendance):
    answer = 0
    ranks = {}
    for idx, value in enumerate(rank):
        if attendance[idx] == True:
            ranks[value] = idx

    ranks = sorted(ranks.items())
    answer = (10000 * ranks[0][1]) + (100 * ranks[1][1]) + ranks[2][1]

    return answer
