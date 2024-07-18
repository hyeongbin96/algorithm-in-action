def solution(num_list, n):
    answer = []
    for i in range(len(num_list) // n):
        result = []
        for j in range(n):
            result.append(num_list[i * n + j])
        answer.append(result)
    return answer