def solution(n):
    answer = [2]
    for i in range(3, n + 1):
        for j in range(2, i + 1):
            if i % j == 0:
                break
            else:
                if j == i - 1:
                    answer.append(i)

    result = []
    idx = 0
    while n > 1:
        if n % answer[idx] == 0:
            result.append(answer[idx])
            n = n // answer[idx]
        else:
            idx = idx + 1

    result = list(set(result))
    result.sort()

    return result