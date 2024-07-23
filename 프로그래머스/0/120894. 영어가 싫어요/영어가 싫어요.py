def solution(numbers):
    eng = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for k, v in enumerate(eng):
        numbers = numbers.replace(v, str(k))

    return int(numbers)