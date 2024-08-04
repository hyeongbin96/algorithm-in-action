def solution(n):
    answer = -1
    for i in range(n + 1):
        if i * i == n:
            answer = (i + 1) ** 2
            break
    return answer

