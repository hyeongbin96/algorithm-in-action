def solution(s, n):
    answer = ""

    for i in s:
        if i == " ":
            answer += " "
        elif i.isupper():
            if ord(i) + n > 90:
                answer += chr(64 + (ord(i) + n - 90))
            else:
                answer += chr(ord(i) + n)
        else:
            if ord(i) + n > 122:
                answer += chr(96 + (ord(i) + n - 122))
            else:
                answer += chr(ord(i) + n)

    return answer