def solution(spell, dic):
    answer = ["".join(sorted(value)) for value in dic if "".join(sorted(spell)) == "".join(sorted(value))]
    
    return 1 if "".join(sorted(spell)) in answer else 2