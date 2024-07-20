def solution(numbers, direction):
    
    if direction == "left":
        numbers.append(numbers.pop(0))
    else:
        numbers = [numbers.pop(-1)] + numbers

    return numbers