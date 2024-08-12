def solution(my_string, indices):
    my_string = list("".join(my_string))
    for i in indices:
        my_string[i] = "*"
    return "".join(i for i in my_string if i != "*")