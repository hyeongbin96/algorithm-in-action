N, K = map(int, (input().split()))
block = [list(map(int, (input().split()))) for i in range(N)]
commands = input()

x, y = 0, 0

for command in commands:
    if command == "U" and [x, y + 1] not in block:
        y += 1
    elif command == "D" and [x, y - 1] not in block:
        y -= 1
    elif command == "R" and [x + 1, y] not in block:
        x += 1
    elif command == "L" and [x - 1, y] not in block:
        x -= 1

print(x, y)
