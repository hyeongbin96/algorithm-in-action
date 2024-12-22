import sys

N = int(sys.stdin.readline())
level = sorted([int(sys.stdin.readline()) for i in range(N)])


def roundUp(x):
    if (x - int(x)) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


except_level = roundUp(N * 0.15)

if N == 0:
    level_sum = 0
    print(level_sum)
else:
    level_sum = sum([level[i] for i in range(except_level, N - except_level)])
    print(roundUp(level_sum / (N - (except_level * 2))))
