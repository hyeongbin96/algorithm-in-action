import sys

m = int(input())
original_score = list(map(int, sys.stdin.readline().split()))
sum = 0

for i in original_score :
    sum += (i/max(original_score))*100

print(sum/m)