num = 1000000
arr = [i for i in range(num+1)] # 인덱싱하기 편하게 0부터 배열 생성

for i in range(2, num+1) :  # 에라토스테네스의 체의 알고리즘을 사용하여 배열을 돌며 소수가 아닌 수는 제거
    if arr[i] == 0 :
        continue
    for j in range(i*i, num+1, i) :
        arr[j] = 0

T = int(input())

for i in range(T) :
    count = 0
    N = int(input())
    for j in range(2, N//2+1) :
        if arr[j] and arr[N-j] :
            count += 1
    print(count)