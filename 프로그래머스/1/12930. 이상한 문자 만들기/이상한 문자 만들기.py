def solution(s):
    answer = ""

    i = 1
    for idx, word in enumerate((s)):
        if word == " ":
            answer += " "
            i = 1
        else:
            if i % 2 == 0:
                answer += word.lower()
                i += 1
            else:
                answer += word.upper()
                i += 1

    return answer