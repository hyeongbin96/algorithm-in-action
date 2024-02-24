line = int(input())

for i in range(1, line+1) :
    print((' '*(line-i)) + ('*'*(i*2-1)))

for j in range(1, line) :
    print(' '*j + ('*'*(((2*line)-2*j-1))))