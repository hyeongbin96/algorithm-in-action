def solution(n_str):
    answer = list("".join(n_str))

    if answer[0] != "0":
        return "".join(answer)
    else:
        while True:
            if answer[0] == "0":
                answer.remove("0")
            else:
                break
        return "".join(answer)