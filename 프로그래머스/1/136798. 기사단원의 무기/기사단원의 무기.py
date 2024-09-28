def solution(number, limit, power):
    answer = []

    for num in range(1, number + 1):
        count = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                count += 1
                if i**2 != num:
                    count += 1
        answer.append(count)

    for i in range(len(answer)):
        if answer[i] > limit:
            answer[i] = power

    return sum(answer)