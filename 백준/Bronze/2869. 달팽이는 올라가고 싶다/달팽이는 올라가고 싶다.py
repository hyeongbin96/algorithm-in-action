import sys

morning, afternoon, high = map(int, sys.stdin.readline().split())

daily = morning - afternoon

if (high - afternoon) % (daily) == 0 :
    print((high - afternoon) // daily)
else :
    print(((high - afternoon) // daily) + 1)