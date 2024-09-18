def solution(left, right):
    answer = 0
    for numbers in range(left, right + 1):
        if len(divisor(numbers)) % 2 == 0:
            answer += numbers
        else:
            answer -= numbers
    return answer


def divisor(numbers):
    nums = []
    for number in range(1, numbers + 1):
        if numbers % number == 0:
            nums.append(number)
    return nums