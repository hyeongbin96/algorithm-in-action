def solution(emergency):
    answer = sorted(emergency, reverse=True)
    result = []
    for i in emergency:
        result.append(answer.index(i) + 1)

    return result


print(solution([3, 76, 24]))
