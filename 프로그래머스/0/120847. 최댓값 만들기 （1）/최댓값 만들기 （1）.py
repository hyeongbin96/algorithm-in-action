def solution(numbers):
    max_num = max(numbers)
    numbers.remove(max(numbers))

    return (max_num * max(numbers))