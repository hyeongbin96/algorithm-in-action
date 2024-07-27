def solution(polynomial):
    polynomial = polynomial.split("+")
    for idx, value in enumerate(polynomial):
        if " " in value:
            polynomial[idx] = value.replace(" ", "")

    answer = ""
    x = 0
    num = 0

    for i in polynomial:
        if "x" in i:
            if i == "x":
                x += 1
            else:
                x += int(i[0:-1])
        else:
            num += int(i)

    if x == 0:
        answer = str(num)
    elif x == 1:
        if num == 0:
            answer = f"x"
        else:
            answer = f"x + {num}"
    else:
        if num == 0:
            answer = f"{x}x"
        else:
            answer = f"{x}x + {num}"

    return answer
