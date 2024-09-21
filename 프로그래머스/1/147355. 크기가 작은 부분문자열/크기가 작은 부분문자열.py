def solution(t, p):
    answer = 0
    t = [i for i in t]
    for i in range(len(t) - len(p) + 1):
        if int(("".join(t[i : i + len(p)]))) <= int(p):
            answer += 1
    return answer