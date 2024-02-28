alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 33, 2
N, B = map(int, input().split())
result = []

while True :
    if N >= B :     # while을 도는동나 N을 B로 나눈 몫이 N 값이 된다.
        remainder = (N % B)         
        result.append(remainder)     
        N = (N // B)
    else :          # N을 B로 나눠가면서 B보다 N이 작아지면 종료하고 이전에 나눠진 몫을 리스트에 추가
        result.append(N)
        break

result.reverse() # 가장 마지막 몫과 나머지 순으로 진법 변환을 해야되므로 리스트를 역순으로 변경

for i in result :
    print(alpha[i], end='')
