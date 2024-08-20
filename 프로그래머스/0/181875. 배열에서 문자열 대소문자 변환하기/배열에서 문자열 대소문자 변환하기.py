def solution(strArr):
    for idx, value in enumerate(strArr):
        if idx % 2 != 0:
            strArr[idx] = value.upper()
        else:
            strArr[idx] = value.lower()
    return strArr