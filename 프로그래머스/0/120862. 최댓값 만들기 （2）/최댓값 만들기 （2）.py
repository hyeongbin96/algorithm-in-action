def solution(numbers):
    # 내 풀이
    # answer = max((v * j) for idx, v in enumerate(numbers) for j in numbers[idx + 1 : len(numbers) + 1])
    
    # 다른 사람 풀이
    numbers.sort(reverse=False)
    answer = max((numbers[0] * numbers[1]), (numbers[-1] * numbers[-2]))
    return answer