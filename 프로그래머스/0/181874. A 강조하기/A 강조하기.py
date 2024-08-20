def solution(myString):
    answer = ""
    for str in myString:
        if str == "a":
            answer += str.replace(str, "A")
        elif str != "A" and str.isupper() == True:
            answer += str.lower()
        else:
            answer += str

    return answer