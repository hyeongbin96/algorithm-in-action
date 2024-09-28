def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    answer = day[(sum(days[: a - 1]) + b) % 7 - 1]

    return answer