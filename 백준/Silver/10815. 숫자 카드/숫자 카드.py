N = int(input())
arr = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

arr.sort()

for now in check:
    s = 0
    end = N - 1
    ans = 0

    while s <= end:
        mid = (s + end) // 2

        if now > arr[mid]:
            s = mid + 1
        elif now == arr[mid]:
            ans = 1
            break
        else:
            end = mid - 1

    print(ans, end=" ")
