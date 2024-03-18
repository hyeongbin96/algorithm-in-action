import math

def is_Prime(num) :
    if num == 0 or num == 1 :
        return False
    else :
        for i in range(2, int(math.sqrt(num)+1)) :
            if num % i == 0 :
                return False
        return True

N = int(input())

for i in range(N) :
    num = int(input())
    while True :
        if is_Prime(num) == True :
            print(num)
            break
        else :
            num += 1