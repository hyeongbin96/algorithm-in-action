import sys

S = list(sys.stdin.readline().rstrip())  # rstrip() = 개행 제외
word = ''
pel = ''

for i in S :
    word += i

S.reverse()

for j in S :
    pel += j

if word == pel :
    print(1)
else :
    print(0)