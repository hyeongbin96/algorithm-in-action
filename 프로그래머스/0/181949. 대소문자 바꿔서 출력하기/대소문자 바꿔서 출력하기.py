str = input()
answer = ""
for i in str:
    if i in "abcdefghijklmnopqrstuvwxyz":
        answer += i.upper()
    else:
        answer += i.lower()

print(answer)
