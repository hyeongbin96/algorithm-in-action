def solution(n):
    answer = 0
    count = 1

    while True:
        if is_two(n).count(1) == is_two(n + count).count(1):
            answer = n + count
            break
        count += 1

    return answer


def is_two(num):
    answer = []

    while True:
        if num // 2 == 0:
            answer.append(num % 2)
            break
        answer.append(num % 2)
        num = num // 2

    answer.reverse()

    return answer