def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                return False
        return True
    return False
