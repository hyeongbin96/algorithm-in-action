result = []

for i in range(1,10001) :
    if i < 10 :
        num = i + (i % 10)
        result.append(num)
    elif i < 100 :
        num = i + (i // 10) + (i % 10)
        result.append(num)
    elif i < 1000 :
        num = i + (i // 100) + ((i // 10) % 10) + (i % 10)
        result.append(num)
    elif i < 10000 :
        num = i + (i // 1000) + ((i // 100) % 10) + ((i // 10) % 10) + (i % 10)
        result.append(num)
    else :
        num = i + 1

for i in range(1, 10001) :
    if i in result :
        pass
    else :
        print(i)