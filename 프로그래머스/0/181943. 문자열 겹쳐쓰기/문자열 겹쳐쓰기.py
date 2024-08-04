def solution(my_string, overwrite_string, s):
    my_string = [i for i in my_string]
    my_string[s : len(overwrite_string) + s] = overwrite_string

    return "".join(my_string)