def solution(d, budget):
    d = sorted(d)
    count = 0
    sum = 0
    for i in d:
        sum += i
        if sum > budget:
            break
        else:
            count += 1

    return count