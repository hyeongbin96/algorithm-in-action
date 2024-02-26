list_a=[]
max_list=[]
for _ in range(9):
    list_a.append(list(map(int,input().split())))

for i in range(9):
    max_list.append(max(list_a[i]))
print((max(max_list)))

for i in range(9):
    for j in range(9):
        if list_a[i][j]==max(max_list):
            print(i+1,j+1)
            break