N = int(input())
S = list((input().split()) for i in range(N))
S = sorted(S, key=lambda x: int(x[1]))

answer = "".join(s[0][int(s[2]) - 1].upper() for s in S)

print(answer)