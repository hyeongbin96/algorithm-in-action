def solution(A, B):
    answer = 0
    A = [i for i in A]
    B = [i for i in B]

    for i in range(len(A)):
        if A == B:
            break
        else:
            A[0], A[1:] = A[-1], A[0:-1]
            answer += 1

    return -1 if answer == len(A) else answer