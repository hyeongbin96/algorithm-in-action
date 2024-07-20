def solution(numbers, k):
    answer = 0
    while k > 1 :
        answer += 2
        answer %= len(numbers)
        k -= 1
    return numbers[answer]