import math

num = 123456 * 2 # 입력 받을 값 N의 최대 범위, 아래 while 문에서 for문을 돌 때 N*2만큼 수행하기에 *2 해주었음
arr = [i for i in range(num+1)] # 인덱싱하기 편하게 0부터 배열 생성
arr[1] = 0  # 1은 소수도 합성수도 아니므로 0으로 초기화 (0의 의미는 소수가 아닌 수)

for i in range(2, num+1) :  # 에라토스테네스의 체의 알고리즘을 사용하여 배열을 돌며 소수가 아닌 수는 제거
    if arr[i] == 0 :    # 소수가 아닌 수, 즉 이미 나누어진 수면 수행하지 않음
        continue
    for j in range(i*i, len(arr), i) :  # 소수일 때, 자기 자신을 제외한 배수는 모두 0(소수가 아닌 수)
        arr[j] = 0

while True :
    result = [] # 입력 값의 범위에 속하는 소수를 저장할 리스트
    N = int(input())
    if N == 0 :
        break
    for i in range(N+1, (N*2)+1) :  # N보다 커야하니 N+1부터 수행
        if arr[i] != 0 :
            result.append(arr[i])
    print(len(result))