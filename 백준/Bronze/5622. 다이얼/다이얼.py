S = input()
sum = 0

for i in range(len(S)) :
    if S[i] in ['A', 'B', 'C'] :
        sum += 3
    elif S[i] in ['D', 'E', 'F'] :
        sum += 4
    elif S[i] in ['G', 'H', 'I'] :
        sum += 5
    elif S[i] in ['J', 'K', 'L'] :
        sum += 6
    elif S[i] in ['M', 'N', 'O'] :
        sum += 7
    elif S[i] in ['P', 'Q', 'R', 'S'] :
        sum += 8
    elif S[i] in ['T', 'U', 'V'] :
        sum += 9
    elif S[i] in ['W', 'X', 'Y', 'Z'] :
        sum += 10

print(sum)