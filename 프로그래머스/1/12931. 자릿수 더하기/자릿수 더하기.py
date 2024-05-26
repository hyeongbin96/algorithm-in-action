def solution(n):
    answer = 0
    S = str(n)

    for i in range(len(S)) :
        answer += int(S[i])

    return answer