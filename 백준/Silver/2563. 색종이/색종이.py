N=int(input())
arr = [[0 for x in range(101)] for y in range(101)]
result = 0

for count in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10) :
        for j in range(y, y+10) :
            arr[i][j] = 1

for i in range(len(arr)) :
    for j in range(len(arr)) :
        if arr[i][j] == 1 :
            result += 1

print(result)