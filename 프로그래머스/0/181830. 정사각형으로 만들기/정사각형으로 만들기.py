def solution(arrs):
    for idx, arr in enumerate(arrs):
        if len(arrs) > len(arrs[idx]):
            for j in range(len(arrs) - len(arrs[idx])):
                arr.append(0)
        else:
            for i in range(len(arrs[0]) - len(arrs)):
                arrs.append([0] * len(arrs[0]))
    return arrs
