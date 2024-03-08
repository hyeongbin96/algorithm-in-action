while True :
    length = list(map(int, input().split()))
    sort_length = (sorted(length))

    if sort_length[0] == 0 or sort_length[1] == 0 or sort_length[2] == 0 :
        break

    elif sort_length[0] == sort_length[1] == sort_length[2] :
        print('Equilateral')

    elif sort_length[2] >= sort_length[0] + sort_length[1] :
        print('Invalid')
    
    else :
        if sort_length[0] == sort_length[1] and sort_length[0] != sort_length[2] or sort_length[0] == sort_length[2] and sort_length[0] != sort_length[1] or sort_length[1] == sort_length[2] and sort_length[0] != sort_length[1] :
            print('Isosceles')
        else : 
            print('Scalene')