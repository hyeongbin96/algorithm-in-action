def solution(array):
    array.sort(reverse=False)
    answer = array[len(array)//2]
    return answer