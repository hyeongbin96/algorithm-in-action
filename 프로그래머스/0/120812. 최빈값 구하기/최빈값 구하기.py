def solution(array):
    result = [0 for i in range(1000)]

    for i in array:
        result[i] += 1

    if result.count(max(result)) == 1:
        answer = result.index(max(result))
    else:
        answer = -1

    return answer