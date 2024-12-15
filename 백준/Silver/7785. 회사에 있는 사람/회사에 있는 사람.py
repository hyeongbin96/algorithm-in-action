n = int(input())

dict = {}
for i in range(n):
    name, status = input().split()
    dict[name] = status

answer = []

for k, v in dict.items():
    if v != "leave":
        answer.append(k)

answer.sort(reverse=True)

for i in answer:
    print(i)
