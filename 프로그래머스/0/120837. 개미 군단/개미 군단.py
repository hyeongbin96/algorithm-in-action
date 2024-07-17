def solution(hp):
    answer = 0

    if hp % 5 == 0:
        answer = hp // 5
    else:
        if hp < 5:
            if hp >= 3:
                answer = (hp // 3) + (hp - 3)
            else:
                answer = hp
        else:
            if (hp % 5) < 3:
                answer = (hp // 5) + (hp - (hp // 5) * 5)
            elif (hp % 5) == 3:
                answer = (hp // 5) + 1
            else:
                answer = ((hp // 5) + ((hp - (hp // 5) * 5) // 3) + (hp - (hp // 5) * 5) % 3)

    return answer