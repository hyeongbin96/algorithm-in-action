numbers = []

for i in str(int(input())):
    numbers.append(int(i))

numbers.sort(reverse=True)
answer = ""

for i in numbers:
    answer += "".join(str(i))

print(int(answer))
