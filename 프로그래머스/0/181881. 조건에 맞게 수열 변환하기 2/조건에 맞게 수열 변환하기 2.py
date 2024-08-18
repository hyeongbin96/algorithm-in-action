def solution(arr):
    count = 0
    answer = arr.copy()

    while True:
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1

        if answer == arr:
            break
        else:
            answer = arr.copy()
            count += 1

    return count