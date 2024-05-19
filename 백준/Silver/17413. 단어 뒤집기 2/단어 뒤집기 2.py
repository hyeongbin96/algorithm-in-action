import sys

S = sys.stdin.readline().strip() + ' '
stack = [] 
answer = ''
check = 0 # 괄호 안에 있는지 여부

for i in S : 
    # 문자열이 < 인 경우
    if i == '<' :
        check = 1 # 현재 괄호 안에 있음
        for _ in range(len(stack)) :
            answer += stack.pop()

    stack.append(i)

    # 문자열이 > 인 경우
    if i == '>' :
        check = 0
        for _ in range(len(stack)) :
            answer += stack.pop(0)

    # 문자열이 괄호안에 있지 않고, 공백을 만난 경우
    if (i == ' ') and (check == 0) :
        stack.pop()
        for _ in range(len(stack)) :
            answer += stack.pop()
        answer += ' '

print(answer)