h, m = map(int, input().split())

if h == 0 :
    if 0 <= m < 45 :
        h = 23
        m = m+15
        print(h, m)
    elif 45 <= m < 60 :
        m = m-45
        print(h, m)
elif 1 <= h <= 23 :
    if 0 <= m < 45 :
        h = h-1
        m = m+15
        print(h, m)
    elif 45 <= m < 60 :
        m = m-45
        print(h, m)