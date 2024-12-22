import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

def bfs(tmp_graph):
    q = deque([(j, i) for i in range(N) for j in range(M) if tmp_graph[i][j] == 2])
    while q:
        x, y = q.popleft()
        for nx, ny in zip([x + 1, x - 1, x, x], [y, y, y + 1, y - 1]):
            if 0 <= nx < M and 0 <= ny < N and not tmp_graph[ny][nx]:
                tmp_graph[ny][nx] = 2
                q.append((nx, ny))
                
    global answer
    count = sum([i.count(0) for i in tmp_graph])
    answer = max(answer, count)

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
x_y = [(x, y) for x in range(N) for y in range(M) if not graph[x][y]]
answer = 0

for c in combinations(x_y, 3):
    tmp_graph = deepcopy(graph)
    for x, y in c:
        tmp_graph[x][y] = 1
    bfs(tmp_graph)

print(answer)