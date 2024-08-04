# def solution(n):
#     answer = 1
#     for i in range(1, n // 2 + 1):
#         sum = i
#         for j in range(i + 1, n // 2 + 2):
#             sum += j
#             if sum == n:
#                 print(f"{i} 부터 {j}까지의 합계 = {sum}")
#                 answer += 1

#     return answer


def solution(n):
    answer = 1
    for i in range(1, n // 2 + 1):
        sum = 0
        while sum < n:
            sum += i
            if sum == n:
                answer += 1
                break
            i += 1

    return answer


# print(solution(15))
# print(solution(30))
