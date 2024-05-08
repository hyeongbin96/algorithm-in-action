N = input()
number = [0 for i in range(10)]

for i in N :
    if i == '6' or i == '9' :
        if number[6] > number[9] :
            number[9] += 1
        else :
            number[6] += 1
    else :
        number[int(i)] += 1

print(max(number))