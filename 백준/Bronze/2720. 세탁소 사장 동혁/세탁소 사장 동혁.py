T = int(input())

change = [25, 10, 5, 1]
result = [0, 0, 0, 0]

for i in range(T) :
    C = int(input())
    for j in range(len(change)) :
        result[j] = (C // change[j])
        C = (C % change[j])
    print(*result)