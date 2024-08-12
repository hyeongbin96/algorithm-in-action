def solution(my_string):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    answer = [0] * len(alpha)

    for i in my_string:
        answer[alpha.index(i)] += 1

    return answer