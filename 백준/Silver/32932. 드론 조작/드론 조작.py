N, K = map(int, (input().split()))
block = [list(map(int, (input().split()))) for i in range(N)]
commands = input()

x, y = 0, 0


for command in commands:
    if command == "U":
        if [x, y + 1] in block:
            pass
        else:
            y += 1
    elif command == "D":
        if [x, y - 1] in block:
            pass
        else:
            y -= 1
    elif command == "R":
        if [x + 1, y] in block:
            pass
        else:
            x += 1
    else:
        if [x - 1, y] in block:
            pass
        else:
            x -= 1

print(x, y)
