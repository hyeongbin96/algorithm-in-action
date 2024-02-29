N = int(input())

count = 1   # 시작하는 방도 지나간 방의 개수에 포함하니 무조건 1번방은 포함되므로 초기값은 1
sum = 1     # 이웃하는 방의 개수. 이웃하는 방은 6의 배수를 더한만큼 늘어남 1, 7, 19, 37 ...

if N == 1:      
    count = 1
else :
    while N > sum :     # 입력 값이 방의 범위를 벗어나면 종료
        sum += (6*count)
        count += 1

print(count)
