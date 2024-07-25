def solution(quiz):
    answer = []
    for i in quiz:
        calc = i.split(" ")
        if "+" in calc:
            if int(calc[0]) + int(calc[2]) == int(calc[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(calc[0]) - int(calc[2]) == int(calc[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer