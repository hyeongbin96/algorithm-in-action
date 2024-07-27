def solution(numbers):
    answer = []
    for idx, v in enumerate(numbers):
        for j in numbers[idx + 1 : len(numbers) + 1]:
            answer.append(v * j)

    return max(answer)