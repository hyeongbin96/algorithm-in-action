# 입력 받은 수를 42로 나눈 나머지들을 리스트에 넣고 중복을 제거한 후 리스트의 카운트를 출력하면 될듯
# set() 함수는 리스트의 고유값을 집합으로 반환
result = []

for i in range(1, 11) :
    number = (int(input()) % 42)
    result.append(number)

print(len(set(result)))