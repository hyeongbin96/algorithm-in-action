def solution(numbers):
    answer = ""
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(len(eng)):
        if eng[i] in numbers:
            numbers = numbers.replace(eng[i], str(i))

    return int(numbers)