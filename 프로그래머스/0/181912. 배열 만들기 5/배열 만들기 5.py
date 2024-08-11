def solution(intStrs, k, s, l):
    answer = []
    for strs in intStrs:
        if int(strs[s : s + l]) > k:
            answer.append(int(strs[s : s + l]))
    return answer