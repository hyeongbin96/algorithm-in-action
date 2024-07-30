def solution(numlist, n):
    answer = []
    # -num인 이유 = sort()할 때 첫번째 요소가 같으면 두번째 요소 기준으로 오름차순이기 때문
    numlist = [(abs(n - num), -num) for num in numlist]
    numlist.sort()
    print(numlist)

    for diff, num in numlist:
        answer.append(-num)
    return answer