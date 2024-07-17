def solution(emergency):
    lst0 = emergency.copy()
    lst1 = sorted(emergency, reverse=True).copy()
    for idx, num in enumerate(lst1):
        if num in lst0:
            emergency.__setitem__(lst0.index(num), idx+1)
    return emergency