def solution(numbers):
    return max((v * j) for idx, v in enumerate(numbers) for j in numbers[idx + 1 : len(numbers) + 1])