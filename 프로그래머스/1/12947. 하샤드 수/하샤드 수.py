def solution(x):
    answer = sum([int(i) for i in str(x)])
    if x % answer == 0:
        return True
    return False