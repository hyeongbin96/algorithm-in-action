def solution(myString, pat):
    word = "".join(["B" if i == "A" else "A" for i in myString])
    return 1 if pat in word else 0