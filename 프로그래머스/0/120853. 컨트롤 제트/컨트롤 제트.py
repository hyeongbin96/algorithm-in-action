def solution(s):
    answer = 0
    s = s.split(" ")
    for idx in range(len(s)):
        if s[idx] != "Z":
            answer += int(s[idx])
        else:
            answer = answer - int(s[idx - 1])
    return answer