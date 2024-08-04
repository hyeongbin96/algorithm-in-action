def solution(s):
    arr = []
    for i in s:
        if i == "(":
            arr.append(i)
        else:
            if len(arr) == 0 or arr.pop() != "(":
                return False

    return True if len(arr) == 0 else False