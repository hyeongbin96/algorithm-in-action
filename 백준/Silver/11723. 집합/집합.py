import sys

S = []
M = int(sys.stdin.readline())

for _ in range(M):
    order = sys.stdin.readline().split()
    command = order[0]
    if len(order) == 2:
        x = int(order[1])

    if command == "add":
        if x in S:
            pass
        else:
            S.append(x)

    if command == "remove":
        if x in S:
            S.remove(x)
        else:
            pass

    if command == "check":
        if x in S:
            print(1)  
        else:
            print(0)

    if command == "toggle":
        if x in S:
            S.remove(x)
        else:
            S.append(x)    

    if command == "all":
        S.clear()
        S.extend(range(1, 21))

    if command == "empty":
        S.clear()