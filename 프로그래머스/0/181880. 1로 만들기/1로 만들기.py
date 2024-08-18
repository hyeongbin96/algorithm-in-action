def solution(num_list):
    answer = 0
    for num in num_list:
        answer += make_num(num)
        
    return answer


def make_num(num):
    count = 0
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (num - 1) // 2
        count += 1
    return count