N = int(input())
result = []

for i in range(N) :
    result.append(int(input()))
result.sort(reverse=False) # 리스트 정렬(오름차순(True)이 기본), 내림차순 정렬 = sort(reverse=True)

for i in result :
    print(i)