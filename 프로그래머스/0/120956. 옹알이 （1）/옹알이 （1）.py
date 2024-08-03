def solution(babbling):
    for i in range(len(babbling)):
        for say in ["aya", "ye", "woo", "ma"]:
            if say in babbling[i]:
                babbling[i] = babbling[i].replace(say, " ")
        babbling[i] = babbling[i].replace(" ", "")
    return babbling.count("")
