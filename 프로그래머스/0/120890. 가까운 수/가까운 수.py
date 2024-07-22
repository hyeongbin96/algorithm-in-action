def solution(array, n):
    answer = []
    result = [abs(n - i) for i in array]

    for i in range(len(result)):
        if result[i] == min(result):
            answer.append(array[i])
            
    return min(answer)