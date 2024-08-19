def solution(myString, pat):
    myString, pat = myString.upper(), pat.upper()
    return 1 if pat in myString else 0