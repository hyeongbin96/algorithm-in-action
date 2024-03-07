x, y, w, h = map(int, input().split())

top = h-y
bottom = y-0
right = w-x
left = x-0

a = [top, bottom, right, left]
print(min(a))