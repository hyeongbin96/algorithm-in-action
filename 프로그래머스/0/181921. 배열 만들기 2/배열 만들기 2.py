def solution(l, r):
    answer = []

    for i in range(l, r + 1):
        if i % 5 == 0:
            answer.append(i)

    for i in range(len(answer)):
        if (
            "1" in str(answer[i])
            or "2" in str(answer[i])
            or "3" in str(answer[i])
            or "4" in str(answer[i])
            or "6" in str(answer[i])
            or "7" in str(answer[i])
            or "8" in str(answer[i])
            or "9" in str(answer[i])
        ):
            answer[i] = "*"

    return (
        [-1]
        if len(([i for i in answer if i != "*"])) == 0
        else [i for i in answer if i != "*"]
    )
