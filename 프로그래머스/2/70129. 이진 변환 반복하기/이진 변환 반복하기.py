def solution(s):
    answer = [0, 0]

    while s != "1":
        answer[1] += s.count("0")
        s = s.replace("0", "")
        answer[0] += 1
        s = is_two(len(s))

    return answer


# 2진수로 변환하는 함수
def is_two(num):
    answer = []
    while num > 0:
        answer.append(num % 2)
        num = num // 2
        if num // 2 == 1:
            answer.append(num % 2)
            answer.append(num // 2)
            break
    answer.reverse()

    return "".join(str(i) for i in answer)