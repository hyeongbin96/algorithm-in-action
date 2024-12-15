N, M = map(int, input().split(" "))
S = [input() for i in range(N)]
check = [input() for i in range(M)]

ans = 0
for word in check:
    if word in S:
        ans += 1

print(ans)
