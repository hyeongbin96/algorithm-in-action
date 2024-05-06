K = int(input())

result = []

for _ in range(K) :
    num = int(input())
    if num == 0 :
        result.pop()
    else :
        result.append(num)

print(sum(result))