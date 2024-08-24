def solution(arr, k):
    answer = []

    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
        else:
            continue

    return answer[:k] if len(answer) > k else (answer + [(-1) for i in range(k - len(answer))])