def solution(my_string, num1, num2):
    my_string = list("".join(my_string))
    fir, sec = my_string[num1], my_string[num2]
    my_string[num1] = sec
    my_string[num2] = fir
    return "".join(my_string)