def solution(num_list):
    answer = ["", ""]
    for i in num_list:
        if i % 2 == 0:
            answer[0] += str(i)
        else:
            answer[1] += str(i)
    return int(answer[0]) + int(answer[1])