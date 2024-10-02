def solution(nums):
    answer = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if is_primenumber(nums[i] + nums[j] + nums[k]) == True:
                    answer += 1
                else:
                    answer += 0
    return answer


def is_primenumber(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
