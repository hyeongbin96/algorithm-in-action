def solution(common):
    answer = [common[i] - common[i - 1] for i in range(1, len(common))]

    return ((common[-1] + answer[0]) if answer[0] == answer[1] else (common[-1] * answer[1] // answer[0]))