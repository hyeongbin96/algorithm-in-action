def solution(A, B):
    answer = -1
    A = [i for i in A]
    B = [i for i in B]

    for i in range(len(A)):
        if A == B:
            return i
        A[0], A[1:] = A[-1], A[0:-1]
    return answer