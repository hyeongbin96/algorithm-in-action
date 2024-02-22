# 파이썬 리스트 역순 출력 = list[3:0:-1] > 3번 인덱스부터 1번 인덱스까지 역순 출력
# i ~ j 까지 바구니 번호를 바꿔줘야 하므로 baskte[i-1:j] 을 temp어 넣고 temp.reverse() 함수로 역순을 만든 후 basket[i-1:j] = temp로 업데이트
n, m = map(int, input().split())

basket = [i for i in range(1, n+1)]

for count in range(m) :
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

print(*basket)