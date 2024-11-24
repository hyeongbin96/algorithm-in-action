def num(n, i):
    answer = ""
    while True:
        if i >= 2:
            answer += str(i % 2)
            i = i // 2
        else:
            answer += str(i % 2)
            break

    if len(answer) < n:
        answer = answer + ("0" * (n - len(answer)))

    return answer[::-1]


def solution(n, arr1, arr2):
    # answer = []
    map1 = [num(n, i) for i in arr1]
    map2 = [num(n, i) for i in arr2]
    map = []

    for i in range(n):
        temp = ""
        for j in range(n):
            if (map1[i][j]) == "1" or (map2[i][j]) == "1":
                temp += "#"
            else:
                temp += " "
        map.append(temp)

    return map