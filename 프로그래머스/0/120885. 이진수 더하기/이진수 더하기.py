def solution(bin1, bin2):

    answer = []
    num = is_number(bin1) + is_number(bin2)

    while num > 0:
        answer.append(num % 2)
        num = num // 2

    answer.reverse()

    return "".join([str(i) for i in answer]) if answer else "0"


def is_number(num):  # 2진수 > 10진수로 변환
    number = 0

    for i in range(len(num)):
        if num[i] == "1":
            number += 2 ** (len(num) - 1 - i)

    return number
