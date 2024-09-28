def solution(nums):
    pocket = len(nums) // 2
    nums = list(set(nums))

    if pocket < len(nums):
        return pocket
    else:
        return len(nums)