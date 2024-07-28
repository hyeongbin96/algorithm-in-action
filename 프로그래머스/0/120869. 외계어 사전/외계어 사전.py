def solution(spell, dic):
    for value in dic:
        if sorted(spell) == sorted(value):
            # print(sorted(spell), sorted(value))
            return 1
        # print(sorted(spell), sorted(value))

    return 2