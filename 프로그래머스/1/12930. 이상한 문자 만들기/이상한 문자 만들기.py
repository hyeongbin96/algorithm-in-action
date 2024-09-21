def solution(s):
    answer = ""

    i = 0
    for word in s:
        if word == " ":
            answer += " "
            i = 0
        else:
            if i % 2 == 0:
                answer += word.upper()
                i += 1
            else:
                answer += word.lower()
                i += 1

    return answer


# print(solution("try hello world"))
