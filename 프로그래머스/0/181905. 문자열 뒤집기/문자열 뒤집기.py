def solution(my_string, s, e):
    my_string = list("".join(my_string))
    answer = my_string[s : e + 1]
    answer.reverse()
    print(answer)
    my_string[s : e + 1] = answer
    return "".join(my_string)