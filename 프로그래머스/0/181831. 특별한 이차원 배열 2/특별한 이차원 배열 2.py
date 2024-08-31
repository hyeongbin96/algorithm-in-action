def solution(arr):
    answer = 1
    for i in range(0, len(arr) - 1):
        if arr[i][i + 1] != arr[i + 1][i]:
            return 0

    return answer