def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        strs = ""
        for j in range(i, len(my_string)):
            strs += my_string[j]
        answer.append(strs)

    return sorted(answer)

# def solution(my_string):
#     return sorted([my_string[i:] for i in range(len(my_string))])
