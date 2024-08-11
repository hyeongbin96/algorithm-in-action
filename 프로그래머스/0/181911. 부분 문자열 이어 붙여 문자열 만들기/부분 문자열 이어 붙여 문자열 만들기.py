def solution(my_strings, parts):
    answer = ""
    count = 0
    while count < len(my_strings):
        answer += my_strings[count][parts[count][0] : parts[count][1] + 1]
        count += 1
    return answer
