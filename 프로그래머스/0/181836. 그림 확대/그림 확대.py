def solution(pictures, k):
    answer = []
    for picture in pictures:
        result = ""
        for j in picture:
            result += j * k
        for i in range(k):
            answer.append(result)

    return answer
