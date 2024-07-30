def solution(lines):
    answer = {}

    for i in range(len(lines)):
        for j in range(lines[i][0], lines[i][1]):
            if j not in answer:
                answer[j] = 0
            answer[j] += 1

    return sum(1 for i in answer.values() if i > 1)