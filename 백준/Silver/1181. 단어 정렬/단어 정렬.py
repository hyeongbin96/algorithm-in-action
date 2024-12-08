import sys

N = int(input())
answer = []

for i in range(N):
    word = sys.stdin.readline().rstrip()
    answer.append(word)

a = set(answer)
answer = list(a)
answer.sort(key=lambda x: (len(x), x))

for i in answer:
    print(i)
