import sys

# 2 3
N, M= map(int, sys.stdin.readline().split()) # type: ignore

array = []
dp = [[0] * (M+1) for _ in range(N+1)]

# 1 2 4
# 8 16 32
for i in range(N) :
    array.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N + 1) :
    for j in range(1, M + 1) :
        dp[i][j] = (array[i-1][j-1]) + (dp[i][j-1]) + (dp[i-1][j]) - (dp[i-1][j-1])

K = int(sys.stdin.readline())

for i in range(K) :
    # 1 1 2 3
    i, j, x, y = map(int, sys.stdin.readline().split())
    print((dp[x][y]) - (dp[x][j-1]) - (dp[i-1][y]) + (dp[i-1][j-1]))