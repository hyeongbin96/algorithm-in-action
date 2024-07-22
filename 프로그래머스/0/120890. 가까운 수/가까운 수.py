def solution(array, n):
    array.sort()
    answer = []
    answer = [abs(n - i) for i in array]
            
    return array[answer.index(min(answer))]