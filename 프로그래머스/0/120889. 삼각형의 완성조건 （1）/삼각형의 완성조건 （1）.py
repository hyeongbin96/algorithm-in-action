def solution(sides):
    answer = 0
    max_line = max(sides)
    sides.remove(max(sides))

    if max_line < sum(sides):
        answer = 1
    else:
        answer = 2    
    return answer