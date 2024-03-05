M = int(input())
N = int(input())
print_number = []

for i in range(M, N+1) :
    for j in range(2, i+1) :
        if i % j == 0 :
            if i == j :
                print_number.append(j)
            else :
                break

if sum(print_number) == 0 :
    print(-1)
else :
    print(sum(print_number))
    print(min(print_number))