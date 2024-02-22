# student = [for in range(1, 31)] 로 간단하게 리스트를 채울 수 있음
student = [i for i in range(1, 31)]
no_homework = []

for i in range(1, 29) :
    number = int(input())
    if number in student :
        student.remove(number)

print(min(student))
print(max(student))



# 다른 사람 풀이
import sys

s = [int(sys.stdin.readline().rstrip()) for i in range(28)]
n = [i for i in range(1, 31)]

for i in s :
    if i in n :
        n.remove(i)

print(min(n))
print(max(n))