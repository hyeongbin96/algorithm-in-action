def solution(my_string):
    answer = "".join([i if i.isdigit() else " " for i in my_string])
    return sum(map(int, answer.split()))
