length = list(map(int, input().split()))
sort_length = (sorted(length))

if sort_length[0] == sort_length[1] == sort_length[2] :
    print(sum(sort_length))

elif sort_length[2] < sort_length[0] + sort_length[1] :
    print(sum(sort_length))

elif sort_length[2] >= sort_length[0] + sort_length[1] :
    sort_length[2] = (sort_length[0] + sort_length[1]) - 1
    print(sum(sort_length))