def solution(food):
    answer = ""

    for i in range(1, len(food)):
        if food[i] < 2:
            continue
        elif food[i] % 2 == 0:
            answer += str(i) * (food[i] // 2)
        else:
            answer += str(i) * (food[i] // 2)
            
    return answer + "0" + "".join(list(reversed(answer)))