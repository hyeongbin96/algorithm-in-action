def solution(arr):
    num = 0
    while True:
        if (2**num) <= len(arr) <= 2 ** (num + 1):
            if len(arr) == 2 ** num or len(arr) == 2 ** (num + 1):
                break
            else:
                for i in range(2 ** (num + 1) - len(arr)):
                    arr.append(0)
                break
        else:
            num += 1

    return arr