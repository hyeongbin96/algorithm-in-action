import sys

N = int(sys.stdin.readline())

stack = []

def push(num) :
    stack.append(num)

def pop() : 
    if len(stack) == 0 :
        print(-1)
    else :
        print(stack.pop())

def size() :
    print(len(stack))

def empty() :
    if len(stack) == 0 :
        print(1)
    else :
        print(0)

def top() :
    if len(stack) == 0 :
        print(-1)
    else :
        print(stack[-1])

for i in range(N) :
    order = sys.stdin.readline().split()
    if order[0] == 'push' :
        push(int(order[1]))
    elif order[0] == 'pop' :
        pop()
    elif order[0] == 'size' :
        size()
    elif order[0] == 'empty' :
        empty()
    elif order[0] == 'top' :
        top()