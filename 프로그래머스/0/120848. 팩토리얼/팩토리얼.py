def solution(n):
    answer = 1
    num = 1

    while num <= n:
        num = 1
        for i in range(1, answer + 1):
            num *= i
        answer += 1

    return answer - 2