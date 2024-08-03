def solution(before, after):
    before = [i for i in before]
    after = [i for i in after]
    answer = ""

    for i in before:
        if i in after:
            answer += i
            after.remove(i)
        else:
            break

    return 1 if len(answer) == len(before) else 0