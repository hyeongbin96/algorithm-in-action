N = int(input())    # 배달할 설탕 kg

count = N // 5  # 배달할 설탕에서 최대로 가질 수 있는 최초의 5kg 개수

if N % 5 == 0 : # 5의 배수인 경우 바로 출력
    print(N // 5)
else :  # 5의 배수가 아닌 5kg, 3kg 봉지의 개수 조합을 구해야 하는 경우
    while count >= 0 : # 챙길 수 있는 5kg 봉지가 하나도 없어질 때 까지 수행 (0개도 수행)
        sugar = N - (5 * count) # 5kg 봉지를 챙겼을 때 남은 설탕 무게
        if sugar % 3 == 0 : # 5키로 봉지를 챙기고 3kg로 채워지면 각각의 개수 출력 후 종료
            result = count + (sugar // 3)   
            print(result)
            break
        else :  # 5키로 봉투를 제외한 남은 설탕 무게가 3kg로 채울 수 없으면 5kg 봉지의 개수를 하나 줄임
            count -= 1
    else :
        print(-1)
