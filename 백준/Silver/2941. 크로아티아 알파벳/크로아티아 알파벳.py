korean = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']  # 크로아티아 알파벳에 해당되는 단어

S = input()

for i in korean :   # 리스트를 돌면서 크로아티아 알파벳에 해당되는 단어가 입력 문자열에 포함되는 경우 해당 단어를 임의의 한단어로 변경
    if i in S :
        S = S.replace(i, '?')   # replace(변경전 값, 변경할 값)
        
print(len(S))