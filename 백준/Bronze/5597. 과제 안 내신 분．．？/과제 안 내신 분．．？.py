student = []
no_homework = []

for i in range(1, 31) :
    student.append(i)

for i in range(1, 29) :
    k = (int(input()))
    if k in student :
        student.remove(k)

print(min(student))
print(max(student))