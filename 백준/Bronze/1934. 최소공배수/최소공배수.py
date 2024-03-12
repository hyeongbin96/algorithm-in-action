T = int(input())

def Euclidean(a, b):    
    r = b % a
    if r == 0:        
        return a
    return Euclidean(r, a)

for i in range(T) :
    a, b = map(int, input().split())
    gcd = (Euclidean(a, b))
    result = (a*b) / gcd
    print(int(result))