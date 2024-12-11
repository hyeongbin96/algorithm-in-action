import sys

N = int(sys.stdin.readline())
members = []

for i in range(N):
    age, name = sys.stdin.readline().strip().split(" ")
    members.append([int(age), name])

# print(members)
members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])
