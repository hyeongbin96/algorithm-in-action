N = int(input())
person = []
result = []

for i in range(N) :
    weight, height = map(int, input().split())
    person.append([weight, height])

# [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]
for i in range(N) :
    rank = 0
    for j in range(N) :
        if person[i][0] < person[j][0] and person[i][1] < person[j][1] :
            rank += 1
    result.append(rank+1)

print(*result)