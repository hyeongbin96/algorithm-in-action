def solution(n):
    answer = 1
    while n > 0:

        if answer % 3 == 0 or "3" in str(answer):
            answer += 1
            continue
        else:
            answer += 1

        n -= 1

    return answer - 1