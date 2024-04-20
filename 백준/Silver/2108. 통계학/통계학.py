import sys

N = int(sys.stdin.readline())
number = []
count = dict()

for i in range(N) :
    num = int(sys.stdin.readline())
    number.append(num)
    if num in count :
        count[num] += 1
    else :
        count[num] = 1

number.sort()

# 산술 평균
print(round(sum(number) / N)) 

# 중앙 값
print(number[(N // 2)]) 

# 최빈 값
max_count = []
freq = max(count.values())
for k, v in count.items() :
    if v == freq:
        max_count.append(k)
if len(max_count) == 1 :
    print(*max_count)
else :
    print(sorted(max_count)[1])

# 범위
print(number[-1] - number[0])