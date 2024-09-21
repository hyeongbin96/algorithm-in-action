def solution(n):
    answer = trit(n)
    sum = 0
    for i in range(len(answer)):
        sum += (3 ** (len(answer) - (i + 1))) * answer[i]
    return sum


def trit(n):
    answer = []
    if n < 3:
        return [n % 3]
    else:
        while True:
            if (n // 3) < 3:
                answer.append(n % 3)
                answer.append(n // 3)
                break
            answer.append(n % 3)
            n = n // 3
        return answer