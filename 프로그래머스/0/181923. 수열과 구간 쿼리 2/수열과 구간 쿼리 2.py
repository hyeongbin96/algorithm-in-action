def solution(arr, queries):
    answer = []
    num = []
    for s, e, k in queries:
        num = []
        for i in range(s, e + 1):
            if arr[i] > k:
                num.append(arr[i])
        (answer.append(min(num)) if len(num) != 0 else answer.append(-1))

    return answer
