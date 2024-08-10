def solution(my_string, queries):
    my_string = list("".join(my_string))
    for query in queries:
        my_string[query[0] : query[1] + 1] = list("".join(reversed(my_string[query[0] : query[1] + 1])))
    return "".join(my_string)