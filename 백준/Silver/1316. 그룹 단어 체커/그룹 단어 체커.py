N = int(input())
count = N

word = []
for i in range(N) :
    word.append(input())

for s in word :     # COUNT = 0 으로 선언 후 그룹단어면 +1 하는 방식으로 풀었는데 다른 사람의 아이디어로 COUNT = N 으로 선언 후 푸는 방식 참고
    if len(s) == 1 :
        pass
    else :
        for j in range(len(s)-1) :
            if s[j] == s[j+1] :
                pass
            elif s[j] in s[j+1:] :
                count -= 1
                break

print(count)