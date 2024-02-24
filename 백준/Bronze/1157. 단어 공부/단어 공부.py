word = input().upper()
word_list = [0] * 26
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in word :
    word_list[ord(key)-65] += 1

if word_list.count(max(word_list)) > 1 :
    print('?')
else :
    print(alpha[(word_list.index(max(word_list)))])